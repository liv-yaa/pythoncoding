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

    def removeDuplicates(self, nums: List[int]) -> int:
        #Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once
        #Return k after placing the final result in the first k slots of nums.
        #It is guaranteed that the given array is a sorted array.
        # Ex. [1, 1, 1, 2, 2, 3, 3 ] -> [1, 2, 3]

        # First Index is responsible for writing unique values in our input array, while Second Index will read the input array and pass all the distinct elements to First Index. We continue the above steps until the second index reaches the end of an array
        #Check if prev elem is different from current elem.
        # If found different, perform arr[j] = arr[i] and increment j += 1
        # Increment i+=1 until end of array is reached.

        size = len(nums)
        j = 1
        for i in range(1, size):
            # Find unique element
            if nums[i - 1] != nums[i]:
                #updating j in our main array
                nums[j] = nums[i]
                # Incrementing j (insert) count by 1
                j += 1
        return j



# Def of singly - linked list (https://leetcode.com/problems/palindrome-linked-list/description/)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionNode:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = [head.val]
        while head.next:
            head = head.next
            arr.append(head.val)
        print('arr', arr)
        return (arr == arr[::-1])