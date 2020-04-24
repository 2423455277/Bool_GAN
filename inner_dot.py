#coding:utf-8
import numpy as np  

def inner_dot(x, pi):
    sum = 0
    for i in range(5):
        sum += x[i] & pi[i]
    sum = sum % 2
    return sum
