# -*- coding: utf-8 -*-
"""
Created

@author: acer
"""

class Node: 
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next # tham chiếu đến node tiếp theo trong DLL
        self.prev = prev # tham chiếu đến node trước đó trong DLL 
        self.data = data 


class DoublyLinkedList:       
    def __init__(self): 
        self.head = None
        
    # Thêm một node ở đầu danh sách
    def push(self, new_data): 
      
        # 1 & 2: Phân bổ node và đưa vào dữ liệu
        new_node = Node(data = new_data) 
      
        # 3. Thực hiện tiếp theo của node mới làm đầu và trước đó là NULL 
        new_node.next = self.head 
        new_node.prev = None
      
        # 4. thay đổi trước của node đầu thành node mới 
        if self.head is not None: 
            self.head.prev = new_node 
      
        # 5. di chuyển đầu để trỏ đến node mới
        self.head = new_node 
        
    # Đã cho một node là prev_node
    #hãy chèn một node mới vào sau node đã cho 
      
    def insertAfter(self, prev_node, new_data): 
      
        # 1. kiểm tra xem giá trị trước đó có phải là NULL không 
        if prev_node is None: 
            print("This node doesn't exist in DLL") 
            return
      
            #2. phân bổ node & 3. đưa vào dữ liệu 
        new_node = Node(data = new_data) 
      
            # 4. Thực hiện tiếp theo của node mới như tiếp theo của prev_node 
        new_node.next = prev_node.next
      
            # 5. Đặt phần tiếp theo của prev_node làm new_node  
        prev_node.next = new_node 
      
            # 6. Đặt prev_node làm previous của new_node
        new_node.prev = prev_node 
      
            # 7. thay đổi previous của new_node's next node */ 
        if new_node.next is not None: 
            new_node.next.prev = new_node 
        # Thêm một node vào cuối DLL 
    def append(self, new_data): 
      
            # 1. cấp phát node.2 đưa dữ liệu vào
        new_node = Node(data = new_data) 
        last = self.head 
      
            # 3. Nút mới này sẽ là node cuối cùng
            #Vì vậy đặt tiếp theo là NULL
            #  
        new_node.next = None
      
            # 4. Nếu Danh sách được Liên kết trống
            #Đặt nút mới làm đầu
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return
      
            # 5. Else Chuyển cho đến khi đến node cuối cùng  
        while (last.next is not None): 
            last = last.next
      
            # 6. Đổi tiếp theo của node  
        last.next = new_node 
            # 7. Đặt node cuối cùng làm node trước của node mới */ 
        new_node.prev = last 
            
        # This function prints contents of linked list 
    # starting from the given node 
    def printList(self, node): 
        print("\nTruyền theo hướng về phía trước")
        while(node is not None): 
            print(" % d" %(node.data)) 
            last = node 
            node = node.next
      
        print("\nTruyền theo hướng ngược lại")
        while(last is not None): 
            print(" % d" %(last.data))
            last = last.prev 
            
            
# Driver program to test above functions 
  
# Start with empty list 
llist = DoublyLinkedList() 
  
# Insert 6. So the list becomes 6->None 
llist.append(6) 
  
# Insert 7 at the beginning. 
# So linked list becomes 7->6->None 
llist.push(7) 
  
# Insert 1 at the beginning. 
# So linked list becomes 1->7->6->None 
llist.push(1) 
  
# Insert 4 at the end. 
# So linked list becomes 1->7->6->4->None 
llist.append(4) 
  
# Insert 8, after 7. 
# So linked list becomes 1->7->8->6->4->None 
llist.insertAfter(llist.head.next, 8) 
  
print ("DLL đã tạo mới là: ") 
llist.printList(llist.head)