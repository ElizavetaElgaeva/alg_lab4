#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def min_search(l):
    
    minimum = l[0]
    
    for i in range(1, len(l)):
        
        if (minimum > l[i]):
            minimum = l[i]
    
    return minimum

def selection_sort(a):
    
    sort = []
    
    while len(a) != 0:
        m = min_search(a)
        sort.append(m)
        ind = np.where(a == m)
        
        if (ind != len(a) - 1):
            
            for k in range(int(ind[0]), int(a.shape[0]) - 1):
                a[k] = a [k + 1]
        
        a = a[: -1]
        
    return sort    
        
    pass

