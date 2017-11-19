# -*- coding: utf-8 -*-


def mergeSort(arr,l,r):
    print arr
    if l==r:
        return
    mid = l + ((r-l)>>1)
    print mid
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)

def merge(arr,l,mid,r):
    help = []
    i = 0
    p1 = l
    p2 = mid + 1

    while p1 <= mid and p2 <= r:
        if arr[p1] < arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1
    while p1 <= mid:
        help.append(arr[p1])
        p1 += 1
    while p2 <= r:
        help.append(arr[p2])
        p2 += 1
    for i in range(len(help)):
        arr[l + i] = help[i]


def mergeSort_1(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    # left 采用归并排序后形成的有序的新的列表
    left_li = mergeSort_1(alist[:mid])

    # right 采用归并排序后形成的有序的新的列表
    right_li = mergeSort_1(alist[mid:])

    # 将两个有序的子序列合并为一个新的整体
    # merge(left, right)
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    arr = [54, 35, 48, 36, 27, 12, 44, 44, 8, 14, 26, 17, 28]
    sortArr = mergeSort_1(arr)
    # sortArr = bubbleSort(arr)
    print sortArr