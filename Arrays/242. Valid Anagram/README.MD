```python

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


```


```python

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


        if len(s) != len(t):
            return False

        # Dictionaries to count character occurrences
        countS, countT = {}, {}

        # Populate countS for string `s`
        for i in range(len(s)):
            if s[i] in countS:
                countS[s[i]] += 1
            else:
                countS[s[i]] = 1

        # Populate countT for string `t`
        for i in range(len(t)):
            if t[i] in countT:
                countT[t[i]] += 1
            else:
                countT[t[i]] = 1

        # Compare the two dictionaries
        return countS == countT
s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))
```

https://neetcode.io/solutions/valid-anagram 