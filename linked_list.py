"""
Author:         Elaine Chan Yun Ru
Assignment:     PA1_SortingStackQueue
Date:           1/28/2021
Description:    Contains the class to call functions to modify linked lists
"""

#import Node class
from node import Node

class LinkedList(object):
    # constructor for LinkedList class
    def __init__(self):
        # initialize the following 4 class attributes: __head, __tail, __capacity and __size
        self.__head = None
        self.__tail = None
        self.__capacity = 0
        self.__size = 0

    # add item x to list at index i
    # if item is to be added at index 0, push current head of linked list back a node:
    #   if list is empty, item becomes the head and tail of linked list
    #   if list is not empty, item becomes the head of linked list
    # if item is to be added at end of list, push current tail of linked list forward a node:
    #   if list is empty, item becomes the head and tail of linked list
    #   if list is not empty, item becomes the tail of linked list
    # else:
    #   determine the specific position to insert item
    #   iterate through each node of linked list
    #   upon reaching the specified position:
    #       push the current item back a node, insert item
    def add(self, i, x):
        p = Node()
        setattr(p, "_Node__data", x)
        if i == 0:
            p.__setattr__("_Node__next", self.__head)       # Upon inserting a new item into the list, all affected
            if self.__head is not None:                     # nodes and sequence must be updated (what comes after,
                self.__head.__setattr__("Node__prev", p)    # before, etc)
            else:
                self.__tail = p
            self.__head = p
        elif i == self.__size or i == -1:
            p.__setattr__("_Node__prev", self.__tail)
            if self.__tail is not None:
                self.__tail.__setattr__("_Node__next", p)
            else:
                self.__head = p
            self.__tail = p
        else:
            count = 0
            q = self.__head
            while count < i:
                count += 1
                q = q.__getattribute__("_Node__next")
            p.__setattr__("_Node__prev", q.__getattribute__("_Node__prev"))
            p.__setattr__("_Node__next", q)
            setattr(q.__getattribute__("_Node__prev"), "_Node__next", p)
            q.__setattr__("_Node__prev", p)
        self.__size += 1


    # remove item at index i from the list
    # if item is to be remove from beginning of list, return the head of linked list:
    #   if item is the only item in linked list, set head and tail of linked list to None ( to show that it is empty)
    # if item at the end of the list to be removed, return the tail of linked list
    # else:
    #   determine the specific position of which an item to be removed is located
    #   iterate through linked list until reaching the index
    #   upon reaching the position:
    #       remove the item, and push the next item forward a node
    def remove(self, i):
        item = None
        # (should return item from list or NONE if item is not in the list)
        if i == 0:
            p = self.__head                                         # upon removing any item, all affected nodes of items
            self.__head = getattr(p, "_Node__next")                 # have to be updated (what comes after, before etc)
            if self.__head is not None:
                self.__head.__setattr__("_Node__prev", None)
            else:
                self.__tail = None
        elif i == self.__size - 1 or i == -1:
            p = self.__tail
            if self.__tail is not self.__head:
                self.__tail = getattr(self.__tail, "_Node__prev")
                self.__tail.__setattr__("_Node__next", None)
            else:
                self.__tail = None
                self.__head = None
        else:
            p = self.__head
            pos = 0
            while pos < i:
                p = getattr(p, "_Node__next")
                pos += 1
            setattr(getattr(p, "_Node__next"), "_Node__next", getattr(p, "_Node__next"))
            setattr(getattr(p, "_Node__next"), "_Node__prev", getattr(p, "_Node__prev"))
        p.__setattr__("_Node__prev", None)
        p.__setattr__("_Node__next", None)
        self.__size -= 1
        return getattr(p, "_Node__data")

