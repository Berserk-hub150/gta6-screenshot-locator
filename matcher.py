import numpy as np
from PIL import Image
from scipy.signal import fftconvolve


def locate(atlas, patch):
    '''Rank spatially distinct matches using normalized cross-correlation.'''
    a=np.asarray(atlas.convert('L'),dtype=np.float64)
    p=np.asarray(patch.convert('L'),dtype=np.float64)
    h,w=p.shape
    if min(h,w)<8 or h>a.shape[0] or w>a.shape[1]:
        raise ValueError('Crop must be at least 8x8 and fit inside the atlas')
    p=p-p.mean()
    energy=np.sum(p*p)
    if energy<1:
        return []
    def boxsum(x):
        s=np.pad(x.cumsum(0).cumsum(1),((1,0),(1,0)))
        return s[h:,w:]-s[:-h,w:]-s[h:,:-w]+s[:-h,:-w]
    variance=np.maximum(0,boxsum(a*a)-boxsum(a)**2/(h*w))
    denominator=np.sqrt(variance*energy)
    response=fftconvolve(a,p[::-1,::-1],mode='valid')
    score=np.divide(response,denominator,out=np.full_like(response,-1),where=denominator>1e-6)
    radius=max(4,min(h,w)//3)
    ranked=[]
    for _ in range(min(3,score.size)):
        y,x=np.unravel_index(np.argmax(score),score.shape)
        value=float(score[y,x])
        if value < -0.999: break
        ranked.append(dict(x=int(x+w//2),y=int(y+h//2),score=round(min(1.0,value),4)))
        score[max(0,y-radius):y+radius+1,max(0,x-radius):x+radius+1]=-2
    return ranked
