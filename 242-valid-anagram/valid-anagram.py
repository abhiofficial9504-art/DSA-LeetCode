class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        if len(s) != len(t):
            return False

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch in freq:
                freq[ch] -= 1
                if freq[ch] == 0:
                    del freq[ch]
            else:
                return False
        return freq == {}