import numpy as np,pandas as pd
from scipy.signal import hilbert
from numpy.lib.stride_tricks import sliding_window_view
from sklearn.metrics import roc_auc_score
from pathlib import Path
D=Path(__file__).parent
f=pd.read_csv(D/'train_FD001.txt',sep=r'\s+',header=None)
sensors=[2,3,4,7,8,9,11,12,13,14,15,17,20,21]; cols=[4+s for s in sensors]
early=pd.concat([g.iloc[:30] for i,g in f.groupby(0) if i<=60]);mu=early[cols].mean().to_numpy();sd=early[cols].std().to_numpy();sd=np.where(sd<1e-8,1,sd)
records=[]
for eid,g in f.groupby(0):
 x=(g.sort_values(1)[cols].to_numpy()-mu)/sd;n=len(x)
 w=sliding_window_view(x,20,axis=0).transpose(0,2,1)
 d=np.diff(w,axis=1)
 phi=np.log1p(np.abs(d)).mean(axis=(1,2));rms=np.sqrt(np.mean(d*d,axis=(1,2)))
 phase=np.angle(hilbert(w,axis=1));r=np.abs(np.exp(1j*phase).mean(axis=2)).mean(axis=1)
 lo=w.min(axis=1,keepdims=True);hi=w.max(axis=1,keepdims=True)
 b=np.floor((w-lo)/(hi-lo+1e-12)*10).astype(int).clip(0,9)
 counts=np.stack([(b==j).sum(axis=1) for j in range(10)],axis=-1);p=counts/20
 h=-(np.where(p>0,p*np.log(np.maximum(p,1e-15)),0)).sum(axis=-1).mean(axis=1)/np.log(10)
 omega=r*(1-h)
 for k in range(len(w)):records.append((eid,k+20,n-(k+20),omega[k],rms[k],phi[k]))
a=pd.DataFrame(records,columns=['engine','cycle','rul','omega','rms','phi'])
# Three consecutive positive windows: causal persistence filter.
for name in ['omega','rms','phi']:
 val=a[a.engine.between(61,80)]
 # choose direction using validation only (higher = worse)
 v=val[(val.rul>=61)|(val.rul<=30)]
 direction=1 if roc_auc_score((v.rul<=30).astype(int),v[name])>=.5 else -1
 threshold=float(np.quantile(direction*val.loc[val.rul>=61,name],.95))
 rows=[]
 for eid,g in a[a.engine>=81].groupby('engine'):
  score=direction*g[name].to_numpy();raw=score>threshold
  confirmed=np.convolve(raw.astype(int),np.ones(3,dtype=int),'full')[:len(raw)]==3
  # full convolution count 3 consecutive last 3
  rul=g.rul.to_numpy();early=(rul>=61);near=(rul<=30)
  idx=np.where(confirmed)[0]
  first=int(rul[idx[0]]) if len(idx) else None
  early_alert=bool(np.any(confirmed&early));near_alert=bool(np.any(confirmed&near))
  # first warning within RUL 60..1 (and no earlier false warning)
  valid=np.where(confirmed&(rul<=60)&(rul>=1))[0]
  lead=int(rul[valid[0]]) if len(valid) else None
  rows.append(dict(engine=eid,method=name,first_alert_rul=first,early_false_alert=early_alert,detected_last30=near_alert,lead_cycles=lead))
 result=pd.DataFrame(rows)
 print(name,'direction',direction,'threshold',round(threshold,5),'early_false_engines',result.early_false_alert.sum(),'/20','detected_last30',result.detected_last30.sum(),'/20','lead median',result.lead_cycles.median(),'first alert median',result.first_alert_rul.median())
 result.to_csv(D/f'neurocore_{name}_leadtime.csv',index=False)
