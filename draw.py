import math
import torch

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

def point( src, r,c, clr):
    r,c, = int(r), int(c)
    if isinstance(src, torch.Tensor):
        src[r,c] = torch.ByteTensor(clr)
    else:
        src[r,c] = clr
    # Depending on

def gray_to_clr(x):
    return torch.stack( [x,x,x], dim=2)


# Note all the other drawing functions are abstracted based on the single function, draw point.
# If the data structure is different, simply redefine the point drawing algorithm - yh

def line(src, r,c, l, dir, clr=red):
    if dir=='row':
        for i in range(l):
            point(src, r+i,c, clr)
    elif dir=='col':
        for i in range(l):
            point(src, r,c+i, clr)

def tline(src, r,c, l, dir, clr=red):
    k = 2
    if dir=='row':
        line(src,r,c,l,dir,clr)
        for i in range(k):
            line(src,r,c-i,l,dir,clr)
            line(src,r,c+i,l,dir,clr)
    elif dir=='col':
        line(src,r,c,l,dir,clr)
        for i in range(k):
            line(src,r-i,c,l,dir,clr)
            line(src,r+i,c,l,dir,clr)


def bbox(src, r,c, lr, lc, clr=red):
    r_,c_ = r+lr, c+lc
    tline(src, r,c, lr, 'row', clr)
    tline(src, r,c_, lr, 'row', clr)
    tline(src, r,c, lc, 'col', clr)
    tline(src, r_,c, lc+1, 'col', clr)

def square( src, r,c, clr=red):
    point(src, r-1,c-1, clr)
    point(src, r-1,c, clr)
    point(src, r-1,c+1, clr)
    point(src, r,c-1, clr)
    point(src, r,c, clr)
    point(src, r,c+1, clr)
    point(src, r+1,c-1, clr)
    point(src, r+1,c, clr)
    point(src, r+1,c+1, clr)

def thick_point(src,r,c,clr=red):
    K = 5 # Ideal if K is odd
    k = K//2
    for i in range(math.ceil(K/2)):
        line(src,r+i,c-k, K,'col', clr)
        line(src,r-i,c-k, K,'col', clr)