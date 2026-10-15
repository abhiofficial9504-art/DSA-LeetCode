class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_of_t = {}
        freq_of_s = {}
        if len(s) != len(t):
            return False

        for ch in t:
            freq_of_t[ch] = freq_of_t.get(ch, 0) + 1

        for ch in s:
            freq_of_s[ch] = freq_of_s.get(ch, 0) + 1

        if freq_of_t == freq_of_s:
            return True
        else:
            return False 