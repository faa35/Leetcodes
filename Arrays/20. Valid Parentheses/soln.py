class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closing = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        # for key, v in closing.items():
        #     print(key)

        stack = []
        
        for i in range(len(s)):
            if s[i] in closing:
                if (len(stack) != 0) and (stack[-1] == closing[s[i]]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        if len(stack) == 0 :
            return True
        else:
            return False

sol = Solution()

s = "([])"
print(sol.isValid(s)) # True