"""
Author:         Elaine Chan Yun Ru
Assignment:     PA1_SortingStackQueue
Date:           1/28/2021
Description:    Contains the class to call functions related to queues
"""

#import LinkedList
from linked_list import LinkedList

class Queue(object):
    #constructor for Queue class
    def __init__(self):
        #initialize __linkedList attribute here
        self.__linkedList = LinkedList()

    #adds item to rear of queue
    def enqueue(self, x):
        self.__linkedList.add(-1, x)

    #removes item from front of queue
    def dequeue(self):
        #(should return item from end of queue or NONE of queue is empty)
        cap = self.__linkedList.__getattribute__("_LinkedList__capacity")       # as one item is removed, the capacity
        cap += 1                                                                # of the queue increases by 1
        self.__linkedList.__setattr__("_LinkedList__capacity", cap)
        return self.__linkedList.remove(0)

    #returns Boolean of whether queue is currently empty
    def isEmpty(self):
        if self.__linkedList.__getattribute__("_LinkedList__size") == 0:
            return True
        else:
            return False

    #returns Boolean of whether queue is currently full
    def isFull(self):
        if self.__linkedList.__getattribute__("_LinkedList__capacity") == 0:
            return True
        else:
            return False

    #clears the queue
    def clear(self):
        while not self.isEmpty():
            self.__linkedList.remove(0)

    #looks at the item at the end of the queue without removing it
    def poll(self):
        tail = self.__linkedList.__getattribute__("_LinkedList__tail")
        end_val = tail.__getattribute__("_Node__data")
        return end_val