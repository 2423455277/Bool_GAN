#coding:utf-8
import numpy as np
import mmbent

bool_10_pc1 = [[0]*1024 for i in range(600000)]
g = np.load('bool_5.npy')
for i in range(600000):
    bool_10_pc1[i] = mmbent.mmbent(g[i])
    print(i)
np.save('bool_10_pc1.npy', bool_10_pc1)