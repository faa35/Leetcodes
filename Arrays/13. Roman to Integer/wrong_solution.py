#some basic idea
# I=1
# V=5
# X=10
# L=50
# C=100
# D=500
# M=1000
# Roman = [I,V,X,L,C,D,M]

# # if 10 in Roman:
# #     print('yes')

# # for getting the Value of M
# first get the index of M
# and then put that index in Roman list
# print(Roman[Roman.index(M)])
#---------------------------------------

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        I=1
        V=5
        X=10
        L=50
        C=100
        D=500
        M=1000
        Roman = [I,V,X,L,C,D,M]

        res=0

        #  s = MCMXCIV
        #      1000+(1000-100)

        for i in range(len(s)):
            if Roman[Roman.index(s[i])] < Roman[Roman.index(s[i+1])]:
                res += Roman[Roman.index(s[i+1])] - Roman[Roman.index(s[i])]
                i += 2
            else:
                res += Roman[Roman.index(s[i])]
        return res

s = 'MCMXCIV'

print(Solution().romanToInt(s))

# OUTPUT: ValueError: 'M' is not in list

# because the Roman list(Roman = [I,V,X,L,C,D,M]) is not a list of strings but a list of integers

# SO WE WILL USE A DICTIONARY INSTEAD OF A LIST
#                       |
#                    Hashmap