class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        value = set()

        for i in range(len(nums)):
            if nums[i] in value:
                return True
            else:
                value.add(nums[i])

        return False