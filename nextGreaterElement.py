# 496. Next Greater Element I


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #O(n*m)
        # num1Ind = {n:i for i,n in enumerate(nums1)}
        # a = len(nums1)
        # b = len(nums2)
        # res = [-1] * a
        # for i in range(b):
        #     if nums2[i] not in num1Ind:
        #         continue
        #     for j in range(i + 1, b):
        #         if nums2[j] > nums2[i]:
        #             ind = num1Ind[nums2[i]]
        #             res[ind] = nums2[j]
        #             break
        # return res
        
        # O(n + m)
        num1Ind = {n:i for i,n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                ind = num1Ind[val]
                res[ind] = cur
            if cur in num1Ind:
                stack.append(cur)

        return res



if __name__ == "__main__":
    sol = Solution()
    num1 = [4,1,2]
    num2 = [1,3,4,2]
    print("Output is : ", sol.nextGreaterElement(num1,num2))
