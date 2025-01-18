# I=1
# V=5
# X=10
# L=50
# C=100
# D=500
# M=1000
# Roman = [I,V,X,L,C,D,M]
#now we USE DICTIONARY instead of list




# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         Roman ={ 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

#         res=0

#         #  s = MCMXCIV
#         #      1000+(1000-100)

#         for i in range(len(s)):
#             if i<(len(s)-1) and Roman[s[i]] < Roman[s[i+1]]:
#                 res += Roman[s[i+1]] - Roman[s[i]]
#                 i += 2
#             else:
#                 res += Roman[s[i]]
#                 i+=1
#         return res

# s = 'MCMXCIV'

# print(Solution().romanToInt(s))


# problem with this code is you cannot use i+=2 in for loop



class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman ={ 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        res=0
        i=0

        #  s = MCMXCIV
        #      1000+(1000-100)

        while i < len(s):
            if i<(len(s)-1) and Roman[s[i]] < Roman[s[i+1]]:
                res += Roman[s[i+1]] - Roman[s[i]]
                i += 2
            else:
                res += Roman[s[i]]
                i+=1
        return res
    
# Time complexity: O(n)
# Space complexity: O(1)

s = 'MCMXCIV'

print(Solution().romanToInt(s))