#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Merge Sort implementation. The counter is used to return the number of inversions
#when 1 inversion is when A[j] < A[i] and j>i 
def merge(listOne, listTwo, counter):
    indexOne, indexTwo = 0, 0
    finalList = []
    
    while(indexOne < len(listOne) and indexTwo < len(listTwo)):
        if listOne[indexOne] > listTwo[indexTwo]:
            finalList.append(listTwo[indexTwo])
            indexTwo += 1
            counter += len(listOne) - indexOne
        else:
            finalList.append(listOne[indexOne])
            indexOne += 1
    if len(listOne) == indexOne:
        finalList +=  listTwo[indexTwo:]
    else:
        finalList +=  listOne[indexOne:]
    return finalList, counter
    
def merge2(l1,l2):
    x=None
    try:
        x=[l1.pop(0) if l1[0]<l2[0] else l2.pop(0) for i in range(len(l1)+len(l2))]
        return x
    except:
        return x+l2 if len(l1)==0 else x+l1

def merge_sort(myList, counter):
    if len(myList) > 1:
        firstList = myList[:int(len(myList)/2)]
        secondList = myList[int(len(myList)/2):]
        firstList, counter = merge_sort(firstList, counter)
        secondList, counter = merge_sort(secondList, counter)
        myList, counter = merge(firstList, secondList, counter)
    return myList, counter


theList = [1, 5, 3, 8, 0]
print(merge_sort(theList, 0))