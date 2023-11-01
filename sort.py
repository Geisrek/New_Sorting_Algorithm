# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 14:12:09 2023

@author: USER
"""

lst=[11,2,3,7,9,5]
def sort(lst):
    l2=[]
    l3=[]
    size=len(lst)
    if size==2 :
        lst[0],lst[1]=lst[1],lst[0] if lst[1]>lst[0] else lst
        return lst
    if size==0:
        return[]
    Sum=sum(lst)
    Average=Sum/size
    div=size/Sum
    for x in lst:
        if x>Average:
            l2.append(x)
        else:
            l3.append(x)
    return l3+sort(l2)
print(sort(lst))


"""
To combine a collection of numbers, divide the result by the collection size, and then sort the numbers based on this idea, you can follow these steps:

Calculate the combined value by summing all the numbers in the collection.
Divide the combined value by the collection size to get the average.
Create a list of tuples where each tuple consists of a number from the collection and the absolute difference between that number and the average.
Sort the list of tuples based on the absolute difference.
Here's a Python example that demonstrates this idea:
______________________________________________________
def sort_numbers_by_difference(numbers):
    # Calculate the combined value
    combined_value = sum(numbers)
    
    # Calculate the average
    collection_size = len(numbers)
    average = combined_value / collection_size
    
    # Create a list of tuples with numbers and their absolute differences from the average
    number_difference_pairs = [(num, abs(num - average)) for num in numbers]
    
    # Sort the list of tuples based on the absolute differences
    sorted_numbers = [pair[0] for pair in sorted(number_difference_pairs, key=lambda x: x[1])]
    
    return sorted_numbers

# Example usage:
numbers = [5, 2, 8, 1, 7]
sorted_numbers = sort_numbers_by_difference(numbers)
print(sorted_numbers)
In this example, we calculate the average difference between each number and the average value.
 Then, we sort the numbers based on this difference.
 The result is a list of numbers sorted according to their proximity to the average value.
"""