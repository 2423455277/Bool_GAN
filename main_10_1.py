#coding:utf-8
import numpy as np  
import bool_10_walsh
#import bool_8_walsh_op
#import IF_PC_1

#求Walsh谱值
f = np.load('bool_10_pc1.npy')
#wf = bool_8_walsh.walsh(f[545])
#print(wf)
#用于生成Walsh谱值数据集 
wfs = [[0]*1024 for i in range(60000)]
for i in range(60000):
    wfs[i] = bool_10_walsh.walsh(f[i])
    print(i)
    if (i == 5000):
        np.save('bool_10_walsh.npy',wfs)
np.save('bool_10_walsh.npy',wfs)

#Walsh谱反演公式
#f_op = bool_8_walsh_op.walsh_op(wf)
#print("hello")
#print(f_op[2])
#f_op = [int(x) for x in f_op]
#print(f_op)

#判定是否一阶扩散
#alist = [1,2,4,8,16,32,64,128]
#if IF_PC_1.if_pc_1(f_op, alist) == True:
 #   print("是符合一阶扩散的布尔函数")
#else:
#    print("不是符合一阶扩散的布尔函数")