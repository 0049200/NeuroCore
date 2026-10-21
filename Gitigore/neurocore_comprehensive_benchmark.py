import numpy as np, pandas as pd
from scipy.signal import hilbert
from scipy.stats import spearmanr
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from numpy.lib.stride_tricks import sliding_window_view
from pathlib import Path
D=Path(__file__).parent
F={n:pd.read_csv(D/f'train_{n}.txt',sep=r'\s+',header=None) for n in ['FD001','FD003']}
sel=np.array([2,3,4,7,8,9,11,12,13,14,15,17,20,21]); cols=sel+4
ref=F['FD001']; early=pd.concat([g.iloc[:30] for eid,g in ref.groupby(0) if eid<=60]);mu=early[cols].mean().to_numpy();sd=early[cols].std().to_numpy();sd=np.where(sd<1e-8,1,sd)
frames=[]
for dataset,df in F.items():
 for eid,g in df.groupby(0):
  x=(g.sort_values(1)[cols].to_numpy()-mu)/sd;n=len(x)
  for length in (10,20,40):
   if n<length:continue
   w=sliding_window_view(x,length,axis=0).transpose(0,2,1)
   d=np.diff(w,axis=1);phi=np.log1p(np.abs(d)).mean(axis=(1,2));rms=np.sqrt(np.mean(d*d,axis=(1,2)))
   phase=np.angle(hilbert(w,axis=1));r=np.abs(np.exp(1j*phase).mean(axis=2)).mean(axis=1)
   lo=w.min(axis=1,keepdims=True);hi=w.max(axis=1,keepdims=True)
   b=np.floor((w-lo)/(hi-lo+1e-12)*10).astype(int).clip(0,9)
   counts=np.stack([(b==j).sum(axis=1) for j in range(10)],axis=-1);p=counts/length
   h=-(np.where(p>0,p*np.log(np.maximum(p,1e-15)),0)).sum(axis=-1).mean(axis=1)/np.log(10)
   omega=r*(1-h)
   level=np.mean(np.abs(w),axis=(1,2)); trend=np.mean(np.abs(w[:,-1,:]-w[:,0,:]),axis=1)
   std=np.std(w,axis=1).mean(axis=1);mean=np.mean(w,axis=(1,2))
   dd=np.r_[np.nan,np.abs(np.diff(phi))]
   z=pd.DataFrame({'dataset':dataset,'engine':eid,'cycle':np.arange(length,n+1),'rul':np.arange(n-length,-1,-1),'window':length,'omega':omega,'phi':phi,'delta':dd,'r':r,'h':h,'one_minus_h':1-h,'rms':rms,'level':level,'trend':trend,'std':std,'mean':mean})
   frames.append(z)
a=pd.concat(frames,ignore_index=True).dropna()
a['target']=(a.rul<=30).astype(int)
a['eligible']=(a.rul<=30)|(a.rul>=61)
a['split']=np.select([a.engine<=60,a.engine<=80],['train','val'],default='test')
# each window gets evaluated separately; fixed orientation on FD001 validation, no FD003 tuning
rows=[]; alarms=[]
for length in (10,20,40):
 for feature in ['omega','phi','delta','r','h','one_minus_h','rms','level','trend','std','mean']:
  v=a[(a.dataset=='FD001')&(a.split=='val')&(a.window==length)&a.eligible]
  direction=1 if roc_auc_score(v.target,v[feature])>=.5 else -1
  threshold=float(np.quantile(direction*v.loc[v.target==0,feature],.95))
  for ds in F:
   t=a[(a.dataset==ds)&(a.split=='test')&(a.window==length)&a.eligible]
   score=direction*t[feature]; y=t.target
   auc=roc_auc_score(y,score);ap=average_precision_score(y,score)
   recall=float((score[y==1]>threshold).mean());fpr=float((score[y==0]>threshold).mean())
   total=0;early_count=0;timely_count=0;near_count=0;first_timely=[]
   for eid,g in a[(a.dataset==ds)&(a.split=='test')&(a.window==length)].groupby('engine'):
    flag=(direction*g[feature].to_numpy()>threshold).astype(int)
    conf=np.convolve(flag,np.ones(3,dtype=int),'full')[:len(flag)]==3
    rul=g.rul.to_numpy();idx=np.flatnonzero(conf)
    first=int(rul[idx[0]]) if len(idx) else None
    early_count+=bool(np.any(conf&(rul>=61)))
    timely_count+=bool(np.any(conf&(rul>=15)&(rul<=60)))
    near_count+=bool(np.any(conf&(rul<=30)))
    good=np.flatnonzero(conf&(rul>=15)&(rul<=60))
    if len(good):first_timely.append(int(rul[good[0]]))
    alarms.append(dict(dataset=ds,window=length,feature=feature,engine=eid,first_alert_rul=first,early_alert=bool(np.any(conf&(rul>=61))),timely_alert=bool(len(good)),near_alert=bool(np.any(conf&(rul<=30)))))
    total+=1
   rows.append(dict(dataset=ds,window=length,method=feature,AUROC=auc,AUPRC=ap,window_recall=recall,window_FPR=fpr,early_alert_engines=early_count,timely_alert_engines=timely_count,near_alert_engines=near_count,n_engines=total,median_timely_lead=np.median(first_timely) if first_timely else np.nan,FD001_val_direction=direction,FD001_val_threshold=threshold))
# multivariate classifiers, trained on FD001 training engines, fixed on FD003
features=['omega','phi','delta','r','h','rms','level','trend','std','mean']
for length in (10,20,40):
 train=a[(a.dataset=='FD001')&(a.split=='train')&(a.window==length)&a.eligible]
 for name,model in [('LogisticRegression',make_pipeline(StandardScaler(),LogisticRegression(max_iter=600,class_weight='balanced',random_state=42))),('RandomForest',RandomForestClassifier(n_estimators=100,max_depth=7,min_samples_leaf=30,n_jobs=-1,random_state=42)),('HistGradientBoosting',HistGradientBoostingClassifier(max_iter=100,max_leaf_nodes=12,l2_regularization=5,random_state=42))]:
  model.fit(train[features],train.target)
  val=a[(a.dataset=='FD001')&(a.split=='val')&(a.window==length)&a.eligible]
  thresh=float(np.quantile(model.predict_proba(val.loc[val.target==0,features])[:,1],.95))
  for ds in F:
   t=a[(a.dataset==ds)&(a.split=='test')&(a.window==length)&a.eligible]
   score=model.predict_proba(t[features])[:,1];y=t.target.to_numpy()
   early_count=timely_count=near_count=0; leads=[]
   for eid,g in a[(a.dataset==ds)&(a.split=='test')&(a.window==length)].groupby('engine'):
    flag=(model.predict_proba(g[features])[:,1]>thresh).astype(int)
    conf=np.convolve(flag,np.ones(3,dtype=int),'full')[:len(flag)]==3;rul=g.rul.to_numpy()
    early_count+=bool(np.any(conf&(rul>=61)));timely_count+=bool(np.any(conf&(rul>=15)&(rul<=60)));near_count+=bool(np.any(conf&(rul<=30)))
    good=np.flatnonzero(conf&(rul>=15)&(rul<=60))
    if len(good):leads.append(int(rul[good[0]]))
   rows.append(dict(dataset=ds,window=length,method=name,AUROC=roc_auc_score(y,score),AUPRC=average_precision_score(y,score),window_recall=float(np.mean(score[y==1]>thresh)),window_FPR=float(np.mean(score[y==0]>thresh)),early_alert_engines=early_count,timely_alert_engines=timely_count,near_alert_engines=near_count,n_engines=20,median_timely_lead=np.median(leads) if leads else np.nan,FD001_val_direction=1,FD001_val_threshold=thresh))
results=pd.DataFrame(rows);results.to_csv(D/'neurocore_full_benchmark_results.csv',index=False)
pd.DataFrame(alarms).to_csv(D/'neurocore_full_benchmark_engine_alerts.csv',index=False)
print('ROWS',len(a),'TEST ENGINES',20,'COMBINATIONS',len(results));print('20-cycle results:')
print(results[results.window==20][['dataset','method','AUROC','AUPRC','window_FPR','early_alert_engines','timely_alert_engines']].to_string(index=False,float_format=lambda x:f'{x:.3f}'))
print('\nTOP AUROC:');print(results.sort_values('AUROC',ascending=False).groupby('dataset').head(10)[['dataset','window','method','AUROC','window_FPR','early_alert_engines']].to_string(index=False,float_format=lambda x:f'{x:.3f}'))
