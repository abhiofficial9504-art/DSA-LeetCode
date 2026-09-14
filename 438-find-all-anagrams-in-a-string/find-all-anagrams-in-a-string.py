class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        freq_p = {}
        window_freq = {}
        ans = []
        left = 0

        if len(p) > len(s):
            return []

        for ch in p:
            freq_p[ch] = freq_p.get(ch , 0) + 1
        
        for i in range(len(p)):
            ch = s[i]
            window_freq[ch] = window_freq.get(ch, 0) + 1

        if window_freq == freq_p:
            ans.append(left)


        for right in range(len(p), len(s)):
            window_freq[s[right]] = window_freq.get(s[right], 0) + 1
            window_freq[s[left]] -= 1
            if window_freq[s[left]] == 0:
                del window_freq[s[left]]
            left += 1

            if window_freq == freq_p:
                ans.append(left)
        
        return ans

            