class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        ans = 0

        for i in range(len(s)):
            current = roman_map[s[i]]

            if i + 1 < len(s):
                next_value = roman_map[s[i + 1]]

                if current < next_value:
                   ans -= current
                else:
                    ans += current
            else:
                ans += current
        return ans