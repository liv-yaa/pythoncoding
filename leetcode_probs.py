# leetcode_probs.py

class Solution:
    def reverse(self, x:int) -> int:
        #Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
        #Assume -231 <= x <= 231 - 1 and you are not allowed to store 64-bit integers.
        n = str(x)[::-1]
        m = int(n)
        # return n
        print(n, type(n))
        print(m, type(m))
        # not done!

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution = [0,0]
        # return solution
        # Not done
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    def isPalindrome(self, x: int) -> bool:
        # Given an integer x, return true if x is a palindrome, and false otherwise.
        return x >= 0 and x == int(str(x)[::-1])


s = Solution()
# s.reverse(x=123) # 321
# s.reverse(x=-123) # -321
# s.reverse(x=120) # 21


# Def of singly - linked list (https://leetcode.com/problems/palindrome-linked-list/description/)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def printself(self):
        print(self.val)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = [head.val]
        while head.next:
            head = head.next
            arr.append(head.val)
        print('arr', arr)
        return (arr == arr[::-1])
