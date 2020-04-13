#coding:utf-8
import numpy as np

w = np.load('8_whole.npy')
x = np.load('8_whole.npy')
xw = [[0]*256 for i in range(256)]
#wf = [0]*256

def inner_dot():
    #固定w遍历x
    for k in range(256):
        for i in range(256):
            sum = 0
            for j in range(8):
                sum += w[k][j] & x[i][j]
            xw[k][i] = sum % 2

def walsh(f):
    wf = [0]*256
    inner_dot()
    for k in range(256):
        sum = 0
        for i in range(256):
            if (xw[k][i] == 0):
                sum += f[i]
            else:
                sum -= f[i]
        wf[k] = sum/256
    return wf