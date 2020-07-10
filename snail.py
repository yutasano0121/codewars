"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
"""

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]


def snail_answer1(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = list(zip(*array))

        array.reverse()
        print(array)
    return a

snail_answer1(array)

def snail_answer2(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []
