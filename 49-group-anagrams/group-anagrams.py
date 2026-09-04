class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]
        return list(group.values())