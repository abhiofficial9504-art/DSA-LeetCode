class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
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
        