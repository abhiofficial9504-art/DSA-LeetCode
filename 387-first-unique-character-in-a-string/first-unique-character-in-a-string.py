class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        hashMap = {}

        for ch in s:
            hashMap[ch] = hashMap.get(ch, 0) + 1

        for i in range(len(s)):
            if hashMap[s[i]] == 1:
                return i
        return -1