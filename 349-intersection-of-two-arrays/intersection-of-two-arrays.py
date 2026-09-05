class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen = set()
        ans = set()
        for i in range(len(nums1)):
            seen.add(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] in seen:
                ans.add(nums2[i])
        return list(ans)