# -*- coding: utf-8 -*-

def insertSort(arr):
    n = len(arr)
    print 'len:%d'%n
    for i in range(1,n):
        insertRange = range(i)
        insertRange.reverse()
        print '------'
        print insertRange
        for j in insertRange:
            print '比较:%d %d'%(j,j+1)
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def insertSort_1(arr):
    n = len(arr)
    print 'len:%d'%n
    for i in range(1,n):
        print '------'
        j = i -1
        while j>=0:
            print '比较:%d %d' % (j, j + 1)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            j=j-1
    return arr


def insertSort_2(arr):
    n = len(arr)
    print 'len:%d'%n
    for i in range(1,n):
        print '------'
        while i>0:
            print '比较:%d %d' % (i-1, i)
            if arr[i-1]>arr[i]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                i-=1
            else:
                break



if __name__ == '__main__':
    arr = [54, 35, 48, 36, 27, 12, 44, 44, 8, 14, 26, 17, 28]
    sortArr = insertSort_2(arr)
    # sortArr = bubbleSort(arr)
    print sortArr
