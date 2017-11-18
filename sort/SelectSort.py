# -*- coding: utf-8 -*-

def selectSort_1(arr):
    if arr is None or len(arr)<2:
        return arr
    n = len(arr)
    for i in range(n-1):
        minIndex  = i
        for j in range(i+1,n):
            print j
            minIndex = j if arr[j]<arr[minIndex] else minIndex
        arr[minIndex],arr[i]=arr[i],arr[minIndex]
    return arr

if __name__ == '__main__':
    arr = [54, 35, 48, 36, 27, 12, 44, 44, 8, 14, 26, 17, 28]
    sortArr = selectSort_1(arr)
    # sortArr = bubbleSort(arr)
    print sortArr