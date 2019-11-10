#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Simple Implementation of Heap using th heapq library. Heapify will transform the
#list to a heap and then we can use heappop to always get the minimum element
#of the heap. With a simple appending we will get the ordered list. O(n)+O(nlogn)
import heapq 
def heapSort(l):
    something=l[:]
    heapq.heapify(something)
    return [heapq.heappop(something) for i in range(len(l))]

l=[6, 1, 6, 8, 3, 5, 99, 5, 11, 16, 76, 34, 64, 24, 75, 98, 62, 47] 
sortedList=heapSort(l)