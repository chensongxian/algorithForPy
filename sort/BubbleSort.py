# -*- coding: utf-8 -*-

def bubbleSort(arr):
    """冒泡"""
    if arr == None or len(arr)<2:
        return arr
    n = len(arr)
    forRange = range(1,n)
    forRange.reverse()
    print len(arr)
    print forRange
    for e in forRange:
        print '----'
        for i in range(e):
            print '(比较:%d-%d)'%(i,i+1)
            if(arr[i]>arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1]=temp
    return arr

def bubbleSort(arr):
    """冒泡"""
    if arr == None or len(arr)<2:
        return arr
    n = len(arr)
    forRange = range(1,n)
    forRange.reverse()
    print len(arr)
    print forRange
    for e in forRange:
        print '----'
        for i in range(e):
            print '(比较:%d-%d)'%(i,i+1)
            if(arr[i]>arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1]=temp
    return arr
if __name__ == '__main__':
    arr = [54,35,48,36,27,12,44,44,8,14,26,17,28]
    sortArr = bubbleSort(arr)
    # sortArr = bubbleSort(arr)
    print sortArr
