class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1

        for num in hashMap:
            if hashMap[num] == 1:
                return num
