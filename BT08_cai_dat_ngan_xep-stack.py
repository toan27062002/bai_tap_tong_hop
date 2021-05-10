# -*- coding: utf-8 -*-
"""
Created 

@author: acer
"""

class Node:
   def __init__(self, value):
      self.value = value
      self.next = None
 
class Stack:
    
   # Khởi tạo 1 ngăn xếp
   # Sử dụng 1 nút giả đó là
   # dễ dàng hơn để xử lý các trường hợp cạnh.
   def __init__(self):
      self.head = Node("head")
      self.size = 0
 
   #Biểu diễn chuỗi của ngăn xếp
   def __str__(self):
      cur = self.head.next
      out = ""
      while cur:
         out += str(cur.value) + "->"
         cur = cur.next
      return out[:-3]  
 
   # Nhận kích thước hiện tại của ngăn xếp
   def getSize(self):
      return self.size
    
   #Kiểm tra xem ngăn xếp có trống không
   def isEmpty(self):
      return self.size == 0
    
   # Get the top item of the stack(Nhận vật phẩm trên cùng của ngăn xếp)
   def peek(self):
       
      # Sanitary check to see if we
      # Đang xem 1 ngăn xếp trống
      if self.isEmpty():
         raise Exception("Peeking from an empty stack")
      return self.head.next.value
 
   # Push a value into the stack.(Đẩy một giá trị vào ngăn xếp.)
   def push(self, value):
      node = Node(value)
      node.next = self.head.next
      self.head.next = node
      self.size += 1
      
   # Loại bỏ một giá trị khỏi ngăn xếp và trả về.
   def pop(self):
      if self.isEmpty():
         raise Exception("Popping from an empty stack")
      remove = self.head.next
      self.head.next = self.head.next.next
      self.size -= 1
      return remove.value
 

if __name__ == "__main__":
   stack = Stack()
   for i in range(1, 11):
      stack.push(i)
   print(f"Stack: {stack}")
 
   for _ in range(1, 6):
      remove = stack.pop()
      print(f"Pop: {remove}")
   print(f"Stack: {stack}")