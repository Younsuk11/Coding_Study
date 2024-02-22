#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 12:57:13 2023

@author: yeomss
"""

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#%%

L = SinglyLinkedList()
L.insert_node(3)
L.insert_node(4)
type(L.head.data)

#%%

node = L.head
if (node.data % 2) ==1:
    t = node.next
    node.next = t.next
    

#%%
#
# Complete the 'deleteEven' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST listHead as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

class SinglyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_even_nodes(head):
    # 헤드 노드가 없거나 빈 리스트인 경우 처리
    if head is None:
        return None

    # 첫 번째 노드가 짝수인 경우 처리
    while head is not None and head.data % 2 == 0:
        head = head.next

    current = head

    # 현재 노드와 다음 노드를 확인하면서 짝수 노드 삭제
    while current is not None and current.next is not None:
        if current.next.data % 2 == 0:
            current.next = current.next.next
        else:
            current = current.next

    return head

    #%%
    
listHead_count = int(input().strip())
listHead = SinglyLinkedList()

for _ in range(listHead_count):
    listHead_item = int(input().strip())
    listHead.insert_node(listHead_item)

result = deleteEven(listHead.head)

    #%%
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    listHead_count = int(input().strip())

    listHead = SinglyLinkedList()

    for _ in range(listHead_count):
        listHead_item = int(input().strip())
        listHead.insert_node(listHead_item)

    result = deleteEven(listHead.head)

    print_singly_linked_list(result, '\n', fptr)
    fptr.write('\n')

    fptr.close()
