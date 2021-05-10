# -*- coding: utf-8 -*-
"""
Created 

@author: acer
"""

from binarytree import build
values = [9, 4, 2, 6, 7, None, 1, 5, 8]
root = build(values)
print(root)
print(root.preorder) # duyệt cây theo thứ tự trước
print(root.postorder) # duyệt cây theo thứ tự sau