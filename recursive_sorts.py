# recursive_sorts.py
# merge sort, quicksort, hybrid sort
# Strongly suggest you turn off LLMs like
# GitHub Copilot, TabNine, etc. when working on this file.
# Writing a sorting algorithm yourself is the best
# way to learn how it works.
# Modified by: 
from random import randint


# This function assumes both left and right are sorted
# lists, each in ascending order
# This is already done, don't modify it
def merge(left, right):
    # pre-allocate memory for the merged lists
    merged = [None] * (len(left) + len(right))
    left_index = 0
    right_index = 0
    merged_index = 0
    # move the smallest element from left or right to merged
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged[merged_index] = left[left_index]
            left_index += 1
        else:
            merged[merged_index] = right[right_index]
            right_index += 1
        merged_index += 1
    # copy any remaining elements from left
    while left_index < len(left):
        merged[merged_index] = left[left_index]
        left_index += 1
        merged_index += 1
    # copy any remaining elements from right
    while right_index < len(right):
        merged[merged_index] = right[right_index]
        right_index += 1
        merged_index += 1
    return merged


# Sort a list in ascending order using the
# merge sort algorithm including the provided
# merge function above
# lst[:] = ...
# will replace all the elements in the list with 
# whatever is on the right side of the = sign
# Don't return anything, just replace the elements
# in lst with the sorted elements
def merge_sort(lst):
    if len(lst) <= 1:
        return

    midpoint = len(lst) // 2

    left = lst[:midpoint]
    right = lst[midpoint:]

    merge_sort(left)
    merge_sort(right)

    lst[:] = merge(left, right)


# Sorts a list in ascending order using the quicksort algorithm
# between *start* and *end* inclusive
# Meaning if we had a list like [5, 3, 8, 6, 2]
# and we called quicksort_in_place(lst, 1, 3)
# it would result in the list [5, 3, 6, 8, 2]
# Please choose a random pivot index between
# start and end inclusive using randint
# Don't return anything, just sort lst in-place
def quicksort_in_place(lst, start, end):
    #Bottom Layer
    if start >= end:
        return

    # Random pivot
    pivot_index = randint(start, end)

    #Move pivot to end
    lst[pivot_index], lst[end] = lst[end], lst[pivot_index]
    pivot = lst[end]

    smaller_index = start

    for i in range(start, end):
        if lst[i] < pivot:
            lst[i], lst[smaller_index] = lst[smaller_index], lst[i]
            smaller_index += 1

    lst[smaller_index], lst[end] = lst[end], lst[smaller_index]

    quicksort_in_place(lst, start, smaller_index - 1)
    quicksort_in_place(lst, smaller_index + 1, end)


def quicksort(lst):
    quicksort_in_place(lst, 0, len(lst) - 1)


# This is already done, don't modify it
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


# Perform a hybrid sort using the merge sort algorithm
# (although not the merge sort function) for lists
# larger than threshold, and insertion sort for lists
# smaller than or equal to threshold
# Sort in ascending order
# See the note about [:] above merge_sort()
# Don't return anything, just sort lst's items and replace them
def hybrid_sort(lst, threshold=10):
    def hybrid_helper(arr):
        if len(arr) <= threshold:
            temp = arr[:]
            insertion_sort(temp)
            return temp

        midpoint = len(arr) // 2

        left = hybrid_helper(arr[:midpoint])
        right = hybrid_helper(arr[midpoint:])

        return merge(left, right)

    lst[:] = hybrid_helper(lst)
