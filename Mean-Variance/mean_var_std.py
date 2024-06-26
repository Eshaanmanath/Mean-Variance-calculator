import numpy as np

def calculate(a):
    if len(a)!=9:
        raise ValueError("List must contain nine numbers.")
    b=np.array([[a[0],a[1],a[2]],
    [a[3],a[4],a[5]],
    [a[6],a[7],a[8]]])
    calculations={
    'mean':np.array([np.mean(b,axis=0).tolist(),np.mean(b,axis=1).tolist(),np.mean(b)]).tolist(),
    'variance':np.array([np.var(b,axis=0).tolist(),np.var(b,axis=1).tolist(),np.var(b)]).tolist(),
    'standard deviation':np.array([np.std(b,axis=0).tolist(),np.std(b,axis=1).tolist(),np.std(b)]).tolist(),
    'max':np.array([np.max(b,axis=0).tolist(),np.max(b,axis=1).tolist(),np.max(b)]).tolist(),
    'min':np.array([np.min(b,axis=0).tolist(),np.min(b,axis=1).tolist(),np.min(b)]).tolist(),
    'sum':np.array([np.sum(b,axis=0).tolist(),np.sum(b,axis=1).tolist(),np.sum(b)]).tolist(),
    }
    return calculations