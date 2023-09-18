#create a fuction that sorts lists
def sort(nums):
    nums.sort()

'''

'''

#create test cases
#list with random elements
test0 = {
    'input':{'nums':[4, 2, 6, 3, 4, 6, 2, 1]},
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
    }
#list with negative elements
test1 = {
    'input':{'nums':[-4, 2, 6, -3, 4, 6, 2, 1]},
    'output': [-4, -3, 1, 2, 2, 4, 6, 6]
    }

#list in descending order
test2 = {
    'input':{'nums':[42, 36, 19, 15, 7, 6, 3, 1]},
    'output': [1, 3, 6, 7, 15, 19, 36, 42]
    }

#list with no elements

test3 = {
    'input':{'nums':[]},
    'output': []
    }

#list with one element

test4 = {
    'input':{'nums':[4]},
    'output': [4]
    }

#list that's already sorted

test5 = {
    'input':{'nums':[1, 2, 2, 3, 4, 4, 6, 6]},
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
    }

#list with repeated elements

test6 = {
    'input':{'nums':[1, 3, 3, 5, 6, 16, 6, 6, 6, 6, 7, 12, 7, 7, 12, 12]},
    'output': [1, 3, 3, 5, 6, 6, 6, 6, 6, 7, 7, 7, 12, 12, 12, 16]
    }
#list that is very long
'''
to create this final test case we can have a sorted list and then use the range and
shuffle functions to create the input
'''

import random
inputList = list(range(10000))
outputList = list(range(10000))
random.shuffle(inputList)

test7 = {
    'input': {'nums': inputList},
    'output': outputList
    }

tests = [test1, test2, test3, test4, test5, test6, test7]

sort(tests)
