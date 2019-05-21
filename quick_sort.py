#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
#
#def quick_sort(a):
#    
#    if (len(a) <= 1):
#        return a
#    
#    index = np.random.choice(len(a), 1, replace = False) 
#    baseE = a[index]
#    
##    smaller = np.array([i for i in np.delete(a, index) if i < baseE])
##    bigger = np.array([i for i in np.delete(a, index) if i >= baseE])
##    
##    smaller = quick_sort(smaller)
##    bigger = quick_sort(bigger)
##    
##    a = np.concatenate((smaller, baseE, bigger), axis = 0)
    

def quick_sort(a):
    
    def quicksort(a, low, high):
        
        if low < high: 
            p = partition(a, low, high)
            quicksort(a, low, p)
            quicksort(a, p + 1, high)
    
    def partition(a, low, high):
        pivot = a[low]
        while True:
            while a[low] < pivot:
                low += 1
            while a[high] > pivot:
                high -= 1
            if low >= high:
                return high
            a[low], a[high] = a[high], a[low]
            low += 1
            high -= 1
    
    quicksort(a, 0, len(a) - 1)
    return a
        
pass