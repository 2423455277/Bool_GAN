#coding:utf-8
import numpy as np

w = np.load('10_whole.npy')
x = np.load('10_whole.npy')
xw = [[0]*1024 for i in range(1024)]
#wf = [0]*256

def inner_dot():
    #固定w遍历x
    for k in range(1024):
        for i in range(1024):
            sum = 0
            for j in range(10):
                sum += w[k][j] & x[i][j]
            xw[k][i] = sum % 2

def walsh(f):
    wf = [0]*1024
    inner_dot()
    for k in range(1024):
        sum = 0
        for i in range(1024):
            if (xw[k][i] == 0):
                sum += f[i]
            else:
                sum -= f[i]
        wf[k] = sum/1024
    return wf