#coding:utf-8

#f = [0,0,1,1,0,1,0,1]
#alist = [1,2,4]

def Autocorrelation(f, a):
    sum = 0
    for x in range(len(f)):
        if (f[x^a] ^ f[x] == 0):
            sum+=1
        else:
            sum-=1
    #print (sum)
    return sum

def if_pc_1(f,alist):
    answer = True
    for i in range(len(alist)):
        if Autocorrelation(f,alist[i]) != 0:
            answer =False
            #break
    return answer