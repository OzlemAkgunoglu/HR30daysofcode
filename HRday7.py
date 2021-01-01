# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 17:14:00 2020

@author: einst
"""

n=int(input())
arr=list(map(int,input().rstrip.split()))
arr.reverse()
print(*arr)