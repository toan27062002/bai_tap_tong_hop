# -*- coding: utf-8 -*-
"""
Created 

@author: acer
"""

queue = []
 
# Thêm các phần tử vào hàng đợi
queue.append('a')
queue.append('b')
queue.append('c')
 
print("Initial queue")
print(queue)
 
# Xóa các phần tử khỏi hàng đợi
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
 
print("\nQueue after removing elements")
print(queue)