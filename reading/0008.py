'''
Given max() function to find maximum number in the list
But it didn't work as expected
Find the bug and fix it
'''

def max(numbers):
    m = 0
    for n in numbers:
        if m < n:
            n = m
        else:
            m = n

    return m

