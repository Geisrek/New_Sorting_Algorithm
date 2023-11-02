# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 14:12:09 2023

@author: USER
"""
"""This algorithm employs a method that involves the summation of a given list's elements, 
followed by division by its size to calculate the arithmetic mean. Subsequently, 
it compares each element in the list to this computed average value. 
Elements that are less than the computed average are collected into a list denoted as "Less,"
 while those greater than the average are placed in a separate list known as "Greater." This process
 is executed recursively for both the "Less" and "Greater" lists,
 and the results are assigned to the "Left" and "Right" lists, respectively.
The time complexity is O(n logn)"""
lst=[11,2,100,10,7,9,5,5,1,-1]
def averageSort(lst):
    Grater=[]
    Less=[]
    size=len(lst)
    if size<=1:
        return lst
    elif size==2 :
        if lst[0]>lst[1]:
            lst[0],lst[1]=lst[1],lst[0]
        return lst
    #print(lst)
    Sum=sum(lst)
    Average=Sum/size
    for x in lst:
        if x>Average:
            Grater.append(x)
        else:
            Less.append(x)
    lst=averageSort(Less)+averageSort(Grater)
        
    return lst
print(averageSort(lst))
print(lst)




