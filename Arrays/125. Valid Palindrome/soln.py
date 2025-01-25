class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        f = 0
        r = len(s) - 1

        while f < r:
            if not s[f].isalnum():
                f += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[f].lower() == s[r].lower():
                f += 1
                r -= 1
            else:
                return False
        return True        


s = "A man, a plan, a canal: Panama"

sol = Solution()

print(sol.isPalindrome(s)) #True