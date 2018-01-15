#!python
import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_iterative(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if item == array[index]:
        return index
    else:
        if index == len(array) and item != array[index]:
            return None

        # index += 1
        return linear_search_recursive(array, item, index + 1)

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation works
    left = 0
    right = len(array) - 1

    while left <= right:

        #returns approximate middle value
        middle_index = math.floor((left + right) / 2)
        print(middle_index)

        if array[middle_index] == item:
            return middle_index

        elif array[middle_index] < item:
            left = middle_index + 1

        elif array[middle_index] > item:
            right = middle_index - 1


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if left <= right:

        #returns approximate middle value
        middle_index = math.floor((left + right) / 2)

        if array[middle_index] == item:
            return middle_index

        elif array[middle_index] < item:
            left = middle_index + 1
            print(left)
            return binary_search_recursive(array, item, left=left, right=right)

        elif array[middle_index] > item:
            right = middle_index - 1
            return binary_search_recursive(array, item, left=left, right=right)
