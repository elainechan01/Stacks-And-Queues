"""
Author:         Elaine Chan Yun Ru
Assignment:     PA1_SortingStackQueue
Date:           1/28/2021
Description:    Contains the class to call functions related to stacks
"""

#import LinkedList
from linked_list import LinkedList

class Stack(object):
    #constructor for stack class
    def __init__(self):
        #initialize __linkedList attribute here
        self.__linkedList = LinkedList()

    #push item onto stack
    def push(self, x):
        self.__linkedList.add(0, x)

    #pops item from top of stack
    def pop(self):
        #(should return item from top of stack or NONE if stack is empty
        cap = self.__linkedList.__getattribute__("_LinkedList__capacity")   # as one item is removed from stack, the
        cap += 1                                                            # capacity increases by 1
        self.__linkedList.__setattr__("_LinkedList__capacity", cap)
        return self.__linkedList.remove(0)

    #returns Boolean of whether stack is currently empty
    def isEmpty(self):
        if self.__linkedList.__getattribute__("_LinkedList__size") == 0:
            return True
        else:
            return False

    #returns Boolean of whether stack is currently full
    def isFull(self):
        if self.__linkedList.__getattribute__("_LinkedList__capacity") == 0:
            return True
        else:
            return False

    #clears the stack
    def clear(self):
        while not self.isEmpty():
            self.__linkedList.remove(0)

    #looks at the top item of the stack and returns it, without removing it
    def peek(self):
        head = self.__linkedList.__getattribute__("_LinkedList__head")
        top_val = head.__getattribute__("_Node__data")
        return top_val


