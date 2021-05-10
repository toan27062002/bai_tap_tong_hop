# -*- coding: utf-8 -*-
"""
Created 

@author:
"""

from binarytree import build
values = [3, 4, 7,6 , 2, None, 1, 5, 8]
root = build(values)
print(root)
# duyệt cây theo thứ tự trước
print(root.preorder)
# duyệt cây theo thứ tự sau 
print(root.postorder)
