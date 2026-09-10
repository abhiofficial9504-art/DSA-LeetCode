class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        length = 0
        sum_num = 0
        ans = float("inf")
        while right < len(nums):
            if sum_num < target:
                sum_num += nums[right]
                right += 1
            while sum_num >= target:
                length = right - left
                ans = min(ans, length)
                sum_num -= nums[left]
                left += 1
        if ans == float("inf"):
            return 0
        return ans
                


