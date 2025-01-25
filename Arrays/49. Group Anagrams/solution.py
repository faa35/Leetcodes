class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        s ={}

        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str in s:
                s[sorted_str].append(strs[i])
            else:
                s[sorted_str] = [strs[i]]
            
        return list(s.values())


strs = ["eat","tea","tan","ate","nat","bat"]

sol = Solution()
print(sol.groupAnagrams(strs))