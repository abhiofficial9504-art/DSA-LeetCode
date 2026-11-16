class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}

        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1

        for i in range(len(s)):
            if hash_map[s[i]] == 1:
                return i
        return -1