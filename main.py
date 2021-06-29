"""
Author:         Elaine Chan Yun Ru
Assignment:     PA1_SortingStackQueue
Date:           1/28/2021
Description:    Contains the main program of the assignment
"""

#add import statements here
from stack_sorter import StackSorter
from queue_sorter import QueueSorter
from my_stack import Stack
from my_queue import Queue
from linked_list import LinkedList
import copy                             #import python copy module to assist deep copying a list

def main():
    # create instances of StackSorter class, QueueSorter class, Stack class, and Queue class
    sorter1 = StackSorter()
    sorter2 = QueueSorter()
    sorter1b = StackSorter()
    sorter2b = QueueSorter()
    stack1 = Stack()
    stack2 = Stack()
    queue1 = Queue()
    queue2 = Queue()


    # set private linkedList attribute of all instances of stack and queue classes to access all the attributes of
    # LinkedList class
    setattr(stack1, "_Stack__linkedList", LinkedList())
    setattr(stack2, "_Stack__linkedList", LinkedList())
    setattr(queue1, "_Queue__linkedList", LinkedList())
    setattr(queue2, "_Queue__linkedList", LinkedList())


    # hard code 2 different unordered arrays to be then sorted by stack and queue methods
    arr1 = [46,23,51,32,6,5,34,8,25,90,96,83,50,28]     # arr1 to be sorted by stack methods
    ar1 = copy.deepcopy(arr1)                   # create a deep copy of arr1 to be sorted by queue methods
    a_1 = copy.deepcopy(arr1)                   # create a deep copy of arr1 to be displayed when printing output
    arr2 = [44,36,1,4,2,7,5,9,66,3,25,14,97]    # arr2 to be sorted by stack methods
    ar2 = copy.deepcopy(arr2)                   # create a deep copy of arr2 to be sorted by queue methods
    a_2 = copy.deepcopy(arr2)                   # create a deep copy of arr2 to be displayed when printing output


    # call sortArray method from instances of StackSorter and QueueSorter classes
    stack_sort_result = sorter1.sortArray(arr1)
    queue_sort_result = sorter2.sortArray(ar1)
    stack_sort_result_2 = sorter1b.sortArray(arr2)
    queue_sort_result_2 = sorter2b.sortArray(ar2)


    #print results for both sorting calls here
    print(f"Stack sort for argument 1 {a_1}:")
    print(f"{stack_sort_result}\n")
    print(f"Queue sort for argument 1 {a_1}:")
    print(f"{queue_sort_result}\n")
    print(f"Stack sort for argument 2 {a_2}:")
    print(f"{stack_sort_result_2}\n")
    print(f"Queue sort for argument 2 {a_2}:")
    print(f"{queue_sort_result_2}\n")


if __name__ == '__main__':
    main()