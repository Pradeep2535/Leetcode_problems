class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if  m==0:
            nums1.clear()
            nums1[:]=nums2[:]
            
            nums1.sort()
        elif n!=0:
            if n>m:
                nums1[len(nums1)-n:]=nums2[:]
            elif n==m:
                nums1[n:]=nums2[:]
            else:
                nums1[len(nums1)-n:]=nums2[:]

            nums1.sort()
