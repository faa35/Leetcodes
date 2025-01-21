class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        


        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
        #or we can use the below code
        #return sorted(s) == sorted(t)
        
s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))
