class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = float("-inf")
        sum_ele = 0

        for i in range(len(nums)):
            sum_ele += nums[i]
            if maxi < sum_ele:
                maxi = sum_ele
            if sum_ele < 0:
                sum_ele = 0

        return maxi