class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums1=[]
        for i in nums:
            if i not in nums1:nums1.append(i)
        nums.clear()
        nums[::]=nums1[::]
        return len(nums1) 
