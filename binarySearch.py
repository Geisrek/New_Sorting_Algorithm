# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:23:05 2023

@author: USER
"""
def merge(Array,left,right):
    left_size=len(left)
    right_size=len(right)
    i,l,r=0,0,0
    while r<right_size and l<left_size:
        if left[l]<right[r]:
            Array[i]=left[l]
            l+=1 
        else:
            Array[i]=right[r]
            r+=1
        i+=1
    while l<left_size:
        Array[i]=left[l]
        l+=1 
        i+=1
    while r<right_size:
        Array[i]=right[r]
        r+=1
        i+=1
def mergeSort(Array):
    size=len(Array)
    if size<=1:
        return 
    left=Array[:size//2]
    right=Array[len(left):]
    mergeSort(left)
    mergeSort(right)
    merge(Array, left, right)
def binarySearch(Array,item,index=0):
    size=len(Array)
    print(Array,index)
    if size==1 and Array[0]!=item:
        return -1
    middle=Array[size//2]
    print(middle,middle==item,index)
    if middle<item:
        index+=len(Array[:size//2])
        binarySearch(Array[size//2:], item,index)
    elif middle>item:
        index+=len(Array[size//2:])
        binarySearch(Array[:size//2], item,index)
    else:
       return index
Array=[3,5,7,8,1,2,3]
mergeSort(Array)
print(binarySearch(Array,8))
print(Array)