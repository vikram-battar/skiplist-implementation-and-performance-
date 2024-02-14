#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import math
import collections


class Node(object): 
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.up = None
        self.down = None

class SkipListImplementation(object): 
    
    def __init__(self):
        self.elementsCount = collections.Counter()  
        self.root = Node(-math.inf)       
        self.root.right = Node(math.inf)   
        self.height = 1                   

    def findElement(self, target: int) -> bool:
        if(self.elementsCount[target] > 0):
          return target
        else:
          return "Not Exists"
        
    def find(self, num):        
        path = [self.root]
        curr = self.root
        while (curr.right and curr.right.val <= num) or curr.down:
            curr = curr.right if curr.right else curr.down
            path.append(curr)
        return path

    def closestKeyBefore(self, num):
        node = self.root
        t = []
        flag = 0
        while(node.left != None or node.up):
            if node.val == num:
                t =[]
            if node.val < num:
                flag = 1
            t.append(node.val)
        node = node.left
        t.sort()
        if flag == 1:
            return t[-1]
        else:
            print("NULL")
#         return t[-1] if flag == 1 else print("NULL")  

    def closestKeyAfter(self, num):
      node = self.root
      t = []
      flag = 0
      while(node.right != None or node.down):
        if node.val == num:
          flag = 1
        if node.val > num:
          t.append(node.val)
        node = node.right
      t.sort()
      return t[:1] if flag == 1 else print("NULL")    

    def insertElement(self, num): 
        self.elementsCount[num] += 1
        if self.elementsCount[num] > 1:
            return None 
        path = self.find(num) 
        next_node = None
        while path:
            node = Node(num) if (next_node is None) else next_node 
            prev = path.pop()
            node.right = prev.right
            node.left = prev
            prev.right = node
            if node.right: node.right.left = node
            if random.random() <= 0.25: 
                next_node = Node(num)
                node.up = next_node
                next_node.down = node
            else:
                break
            max_height = int(math.log2(len(self.elementsCount)))
            while (self.height <= max_height) and (random.random() <= 0.25): 
                self.height += 1
                next_node = Node(num)
                node.up = next_node
                next_node.down = node
                self.root.up = Node(-math.inf)
                self.root.up.down = self.root
                self.root = self.root.up
                self.root.right = next_node
                next_node.left = self.root
        self.printList()
  
    def removeElement(self, num):
        if self.elementsCount[num] == 0:
            self.printList()
            return "SORRY"
        self.elementsCount[num] -= 1   
        if self.elementsCount[num] >= 1:
            self.printList()
            return num 
        node = self.find(num)[-1] 
        while node and node.left: 
            node.left.right = node.right
            if node.right:
                node.right.left = node.left
            if node.up:
                node = node.up
                node.down = None
            else:
                node = None
        self.printList()
        return num

    def printList(self): 
        x = self.root
        print('\nSKIP LIST IMPLEMENTATION\n\nlevel 0:')
        while(x.right != None):
          print(x.val, end = '->'),
          x = x.right
        print('\n\n\n')
    
    def size(self): 
      nodes = []
      node = self.root
      while(node.right != None or node.down):
        nodes.append(node.val)
        node = node.right
      return len(nodes)-1

list = SkipListImplementation()
print('Skip List Created!')
while(True):
  print('Please Select any one ADT operations:')
  print('1. Find 2. Insert 3. Delete 4. ClosestKeyBefore 5. ClosestKeyAfter 6. Size')
  Operation = int(input())
  if(  Operation== 1):
    print('Enter key to Find: ')
    key = int(input())
    print(list.findElement(key))
  elif(Operation == 2):

    print('Enter Key: ')
    key = int(input())
    list.insertElement(key)
  elif(Operation == 3):
    print('Enter Key:')
    key = int(input())
    print(list.removeElement(key))
  elif(Operation== 4):
    print('Enter key: ')
    key = int(input())
    print(list.closestKeyBefore(key))
  elif(Operation== 5):
    print('Enter key: ')
    key = int(input())
    print(list.closestKeyAfter(key))
  elif(Operation == 6):
    print('Size of theList: ')
    print(list.size())
  else:
    break


# ### 

# In[ ]:




