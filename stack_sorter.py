"""
Author:         Elaine Chan Yun Ru
Assignment:     PA1_SortingStackQueue
Date:           1/28/2021
Description:    Contains the class to call functions to execute a sort method based on stacks
"""

#import Stack
from my_stack import Stack

class StackSorter(object):
    #constructor for StackSorter class
    def __init__(self):
        #initialize attributes __sortedlist
        self.__sortedList = []

    #sort a list of numbers using stacks
    # source code was referred to on geeksforgeeks.org
    def sortArray(self, nums):
        tempStack = Stack()                                                 #create an instance of Stack
        while len(nums) > 0:                                                #iterate through each value of nums until empty
            tempVal = nums.pop()
            while not tempStack.isEmpty() and tempStack.peek() > tempVal:   #compare if value is smaller than the first value of stack
                nums.append(tempStack.pop())                                #if it is, add value to the front of stack
            tempStack.push(tempVal)                                         #if stack is empty, add the last value of nums
        while tempStack.isEmpty() is False:
            self.__sortedList.insert(0, tempStack.pop())                    #assign the new stack to sortedList
        return self.__sortedList






