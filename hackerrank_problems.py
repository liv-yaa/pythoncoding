# hackerrank problems.py
import unittest

# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):
    """
    >>> merge_the_tools('AABCAAADA', 3)
    AB
    CA
    AD
    >>> merge_the_tools('AABCAAADAAAB', 3)
    AB
    CA
    AB

    """
    # Split s into  equal parts of length k. 
    # Convert each ti to ui by removing any subsequent occurrences of non-distinct characters in ti.

    i = 0
    ustrings = []
    
    while i<len(string):
        ti = string[i:i+k]
        i = i+k        
        distinct = ''
        for c in ti:
            if c not in distinct:
                distinct += c
        print(distinct)    
    
    

if __name__ == '__main__':
    unittest.main()