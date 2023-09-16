'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=set(nums)
        l=len(nums)
        d=-1
        for i in a:
            c=nums.count(i)
            if c>l//2 and c>d :
                n=i 
                d=c
        return n    
