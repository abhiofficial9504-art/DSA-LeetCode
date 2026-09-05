class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        window = set()
        left = 0

        for num in nums:
            if num in window:
                return True 
            window.add(num)

            if len(window) > k:
                window.remove(nums[left])
                left += 1
        return False