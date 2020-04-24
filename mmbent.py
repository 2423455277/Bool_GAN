#coding:utf-8
import numpy as np   
import inner_dot
import IF_PC_1

x = np.load('5_whole.npy')
y = np.load('5_whole.npy')
#g = [1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0]
pi = np.load('5_whole.npy')


def mmbent(g):

    f = [0]*1024
    num = 0
    for i in range(32):
        for j in range(32):
            #将二进制数转化为十进制数作为数组下标
            str1 = ''.join(str(k) for k in y[j])
            yj = int(str1,2)
            #求x与置换函数的点积
            xpi = inner_dot.inner_dot(x[i], pi[yj])
            f[num] = xpi ^ g[yj]
            num += 1

    #print(f)
    return f
    #判定是否一阶扩散
    #alist = [1,2,4,8,16,32,64,128]
    #if IF_PC_1.if_pc_1(f, alist) == True:
    #    print("是符合一阶扩散的布尔函数")
    #else:
        #print("不是符合一阶扩散的布尔函数")

#if __name__ == '__main__':
    #g = [1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0]
    #mmbent(g)