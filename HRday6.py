# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:55:45 2020

@author: einst
"""

T=int(input())
for i in range(0,T):
    S=input()
    print(S[0::2],S[1::2])












"""class solution:
    def __init__(self,T,S):
        T=int(input())
        for i in range(0,T):
            S=input()
            evod(S)
    
    def evod(S):
        N=len(S)
        for j in range(0,N-1):
            if j%2==0:
                print(*S[j])
            else:
                print(*S[j])
#print(str(evens),str(odds))"""

