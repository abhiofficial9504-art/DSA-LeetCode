class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        ans = 0
        seen = {}

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) + 1
            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1
            length = right - left + 1
            ans = max(length, ans)
        return ans

