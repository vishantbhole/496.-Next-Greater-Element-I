# 496. Next Greater Element I


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #O(n*m)
        num1Ind = {n:i for i,n in enumerate(nums1)}
        a = len(nums1)
        b = len(nums2)
        res = [-1] * a
