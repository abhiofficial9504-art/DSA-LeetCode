class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel = ['a', 'e', 'i', 'o', 'u']
        left = 0
        count = 0
        
        for i in range(k):
            if s[i] in vowel:
                count += 1

        ans = count

        for i in range(k, len(s)):
            if s[left] in vowel:
                count -= 1

            if s[i] in vowel:
                count += 1

            left += 1

            ans = max(ans, count)
        return ans
            
                    