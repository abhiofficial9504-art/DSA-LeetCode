class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        freq = {}

        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in ransomNote:
            if not ch in freq:
                return False
            freq[ch] -= 1
            if freq[ch] == 0:
                del freq[ch]
        
        return True