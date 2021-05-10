# -*- coding: utf-8 -*-
"""
Created on Tue May  4 08:36:46 2021

@author: acer
"""
# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
 
         #tim phan giua cua mang
        mid = len(arr)//2
 
        # phan chia cac phan tu mang
        L = arr[:mid]
 
        # thanh 2 nua
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # sao chep du lieu vao mang tam thoi L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # kiem tra xem co phan tu nao con lai khong
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
# Code to print the list
 
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("mang da cho la", end="\n")
    printList(arr)
    mergeSort(arr)
    print("mang da sap xep la: ", end="\n")
    printList(arr)
 
# This code is contributed by Mayank Khanna