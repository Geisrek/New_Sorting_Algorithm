# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 15:47:47 2023

@author: USER
"""
def zigzag(s,n):
    lst=[[] for x in range((n))]
    index=0
    step=-1
    if len(s)==1 or index>=len(s):
        return s
    for char in s:
        lst[index].append(char)
        if index==0:
            step=1
        elif index==n-1:
            step=-1
        index+=step 
    return lst
st=input(':')
numrows=int(input(':'))
print(zigzag(st, numrows))
def zigzag2(s,n):
    lst=[[] ]*n
    index=0
    step=-1
    if len(s)==1 or index>=len(s):
        return s
    for char in s:
        lst[index].append(char)
        if index==0:
            step=1
        elif index==n-1:
            step=-1
        index+=step 
    return lst          
        
rows=[[] for x in range(3)]
print(rows)
rows=[[]]*3
print((rows))
print(zigzag2(st, numrows))