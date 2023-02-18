"""

My solution to : https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python

You could solve this in one short line of code. I believe this is one of the most optimal solution.

"""

def find_uniq(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num, count in counts.items():
        if count == 1:
            return num
    for i in arr:
        return n   # n: unique number in the array
