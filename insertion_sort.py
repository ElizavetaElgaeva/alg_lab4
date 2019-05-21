#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertion_sort(a):
     
    for i in range(len(a)):
        tmp = a[i]
        j = i - 1
        
        while j >= 0 and tmp < a[j]:
            a[j+1], a[j] = a[j], a[j+1]
            j -= 1
    
    return(a)
    
    pass
