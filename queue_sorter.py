"""
Author:         Elaine Chan Yun Ru
Assignment:     PA1_SortingStackQueue
Date:           1/28/2021
Description:    Contains the class to call functions to execute a sort method based on queues
"""

#import Queue
from my_queue import Queue

class QueueSorter(object):
    #constructor for QueueSorter class
    def __init__(self):
        #initialize attributes __sortedlist
        self.__sortedList = []

    #sort a list of numbers using queues (bubble sort)
    # swaps 2 adjacent elements until everything is in order
    def sortArray(self, nums):
        tempQueue = Queue()
        for i in nums:
            tempQueue.enqueue(i)            # fill up queue with values from nums
        for x in range(len(nums)):          # determine first value to be compared with
            var1 = tempQueue.dequeue()
            for y in range(len(nums) - 1):  # determine the second value to be compared to (the adjacent value)
                var2 = tempQueue.dequeue()
                if var1 > var2:             # if the first value is smaller than the second value
                    tempQueue.enqueue(var2) # the second value is placed towards the back of the queue
                else:
                    tempQueue.enqueue(var1)
                    var1 = var2
            tempQueue.enqueue(var1)
        while tempQueue.isEmpty() is False:
            self.__sortedList.append(tempQueue.dequeue())       # assign the new queue into the sortedList attribute
        return self.__sortedList


