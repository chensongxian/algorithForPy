# -*- coding: utf-8 -*-

import random

def quickSort(arr,l,r):
    if l >= r:
        return
    p = partition(arr,l,r)
    quickSort(arr,l,p-1)
    quickSort(arr,p,r)
    return arr



def partition(arr,l,r):
    mid = l + (int)( random.random() * (r - l + 1))
    pivot = arr[mid]
    while l<=r:
        while arr[l]<pivot:
            l+=1
        while arr[r]>pivot:
            r-=1
        if l<=r:
            arr[l],arr[r] = arr[r],arr[l]
            l+=1
            r-=1
    return l


def quickSort_1(arr,first,last):
    """快速排序"""
    if first>=last:
        return arr
    mid_value = arr [first]
    low = first
    high = last

    while low < high:
        while low < high and arr[high]>=mid_value:
            high-=1
        arr[low] = arr[high]
        while low < high and arr[low]<mid_value:
            low+=1
        arr[high]=arr[low]
    arr[low] = mid_value
    quickSort_1(arr,first,low-1)
    quickSort_1(arr,low+1,last)
    return arr



def quickSort_3(arr,l,r):
    if l<r:
        mid = l+(int)(random.random()*(r-l+1))
        arr[mid],arr[r]=arr[r],arr[mid]
        p = partition_3(arr,l,r)
        quickSort_3(arr,l,p[0]-1)
        quickSort_3(arr,p[1]+1,r)
    return arr

def partition_3(arr,l,r):
    less = l-1
    more = r
    while l<more:
        if arr[l]<arr[r]:
            less+=1
            arr[less],arr[l] = arr[l],arr[less]
            l+=1
        elif arr[l]>arr[r]:
            more-=1
            arr[more],arr[l] = arr[l],arr[more]
        else:
            l+=1
    arr[more],arr[r] = arr[r],arr[more]
    return [less+1,more]

if __name__ == '__main__':
    arr = [54, 35, 48, 36, 27, 12, 44, 44, 8, 14, 26, 17, 28]
    sortArr = quickSort_3(arr,0,len(arr)-1)
    # sortArr = bubbleSort(arr)
    print sortArr