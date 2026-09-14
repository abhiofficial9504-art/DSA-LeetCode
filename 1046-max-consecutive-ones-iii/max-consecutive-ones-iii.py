class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        ans = 0
        countZero = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                countZero += 1

            while countZero > k:
                if nums[left] == 0:
                    countZero -= 1
                left += 1
            length = right - left + 1
            ans = max(ans, length) 

        return ans