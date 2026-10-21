"""NeuroCore exploratory FD001 benchmark. Run: python neurocore_fd001_test.py train_FD001.txt"""
import sys
import numpy as np
import pandas as pd
from scipy.signal import hilbert
from sklearn.metrics import roc_auc_score, average_precision_score

PATH=sys.argv[1] if len(sys.argv)>1 else 'train_FD001.txt'
df=pd.read_csv(PATH,sep=r'\s+',header=None)
assert df.shape[1]==26, f'Expected 26 columns, got {df.shape[1]}'
# fixed sensor selection before testing; sensor columns start at index 5
SENSORS=[2,3,4,7,8,9,11,12,13,14,15,17,20,21]
cols=[4+s for s in SENSORS]
engines=sorted(df[0].unique())
train_ids=set(engines[:60]); val_ids=set(engines[60:80]); test_ids=set(engines[80:])
WINDOW=20
# Standardize by training engines' early-life (first 30 cycles) only.
early=pd.concat([g.iloc[:min(30,len(g))] for i,g in df.groupby(0) if i in train_ids])
mu=early[cols].mean().to_numpy(); sd=early[cols].std().to_numpy(); sd=np.where(sd<1e-8,1,sd)
records=[]
for eid,g in df.groupby(0):
    g=g.sort_values(1); x=(g[cols].to_numpy()-mu)/sd; n=len(x)
    for end in range(WINDOW,n+1):
        w=x[end-WINDOW:end]
        # Phi: per-channel differences, then mean; avoids flatten boundary artifacts
        phi=np.log1p(np.abs(np.diff(w,axis=0))).mean()
        h=[]
        for j in range(w.shape[1]):
            hist,_=np.histogram(w[:,j],bins=10)
            p=hist[hist>0]/hist.sum()
            h.append(-np.sum(p*np.log(p))/np.log(10))
        h=float(np.mean(h))
        phases=np.angle(hilbert(w,axis=0))
        r=float(np.abs(np.exp(1j*phases).mean(axis=1)).mean())
        omega=r*(1-h)
        # RMS variation baseline, same input window
        rms=float(np.sqrt(np.mean(np.diff(w,axis=0)**2)))
        records.append((eid,end,n-end,phi,omega,rms))
a=pd.DataFrame(records,columns=['engine','cycle','rul','phi','omega','rms'])
a['delta']=a.groupby('engine').phi.diff().abs()
a=a.dropna().copy()
# Label: within 30 cycles of terminal failure. Exclude middle range 31-60
# to make healthy vs near-failure contrast explicit, and not claim exact RUL prediction.
a=a[(a.rul<=30)|(a.rul>=61)].copy()
a['target']=(a.rul<=30).astype(int)
a['split']=a.engine.map(lambda i:'train' if i in train_ids else ('val' if i in val_ids else 'test'))
# Fixed candidate scores; direction and threshold selected on validation, never test.
# Omega direction is not presumed: allow sign selection on validation.
features=['phi','delta','omega','rms']
rows=[]
for feat in features:
    v=a[a.split=='val']; t=a[a.split=='test']
    if v.target.nunique()<2 or t.target.nunique()<2: raise ValueError('Insufficient classes')
    direction=1 if roc_auc_score(v.target,v[feat])>=0.5 else -1
    sv=direction*v[feat].to_numpy(); st=direction*t[feat].to_numpy()
    # threshold at validation healthy 95th percentile; fixed for test
    th=float(np.quantile(sv[v.target.to_numpy()==0],0.95))
    rows.append({'feature':feat,'direction':direction,'validation_threshold':th,
        'test_AUROC':roc_auc_score(t.target,st),
        'test_AUPRC':average_precision_score(t.target,st),
        'test_recall':float(np.mean(st[t.target.to_numpy()==1]>th)),
        'test_false_alarm_rate':float(np.mean(st[t.target.to_numpy()==0]>th))})
result=pd.DataFrame(rows).sort_values('test_AUROC',ascending=False)
result.to_csv('neurocore_fd001_results.csv',index=False)
print('Engines: train 60, validation 20, test 20; test windows',len(a[a.split=='test']))
print(result.to_string(index=False,float_format=lambda z:f'{z:.4f}'))
print('NOTE: retrospective near-failure classification, NOT validated real-time forecasting.')
