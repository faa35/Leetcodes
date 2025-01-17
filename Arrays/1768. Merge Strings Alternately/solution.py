class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result = ""
        
        i = j = 0

        while i < len(word1) and j < len(word2):
            result += word1[i] + word2[j]
            i += 1
            j += 1

        if i < len(word1):
            result += word1[i:]

        elif j < len(word2):
            result += word2[j:]

        return result
        

word1 = "ab"
word2 = "pqrs"

print(Solution().mergeAlternately(word1, word2))