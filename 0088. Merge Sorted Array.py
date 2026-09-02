class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        curr = m + n -1 # Index for insertion
        m, n = m-1, n-1 # Index of the current value in nums1, nums2
        while n>=0:
            if m < 0 or nums1[m] < nums2[n]:
                nums1[curr] = nums2[n]
                n -= 1
            else:
                nums1[curr] = nums1[m]
                m -= 1
            curr -= 1
