# https://cs.stanford.edu/people/nick/py/python-doctest.html

import unittest
def digits_only(s):
    """
    Given a string s.
    Return a string made of all the chars in s which are digits, so 'Hi4!x3' returns '43'.
    >>> digits_only('Hi4!x3')
    '43'
    >>> digits_only('123')
    '123'
    >>> digits_only('')
    ''
    """
    result = ''
    for i in range(len(s)):
        if s[i].isdigit():
            result += s[i]
    return result

if __name__ == '__main__':
    unittest.main()