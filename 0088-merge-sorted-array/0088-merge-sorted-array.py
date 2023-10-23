class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m==0 or nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n = n - 1
            else:
                x = nums1[m-1]
                nums1[m+n-1] = x
                nums1[m-1] = 0
                m = m - 1
                
                
            
        