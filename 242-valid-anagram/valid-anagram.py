class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        if len(s) != len(t):
            return False

        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        for ch in t:
            if ch in seen:
                seen[ch] -= 1
                if seen[ch] == 0:
                    del seen[ch]
        
        return seen == {}
