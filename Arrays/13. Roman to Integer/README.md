# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/description/) 

Below is the step-by-step progression:

---

## Basic Idea

### Roman Numeral Values
```python
# Roman numeral values
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
Roman = [I, V, X, L, C, D, M]
```

### Example Check
```python
# Check if a specific numeral is in the Roman list
# if 10 in Roman:
#     print('yes')
```

### Accessing Roman Numeral Values by Index
```python
# To get the value of M, first get the index of M
# and then put that index in the Roman list
# print(Roman[Roman.index(M)])
```

---

## First Implementation

The initial approach uses a list to represent Roman numeral values:

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        Roman = [I, V, X, L, C, D, M]

        res = 0

        for i in range(len(s)):
            if Roman[Roman.index(s[i])] < Roman[Roman.index(s[i+1])]:
                res += Roman[Roman.index(s[i+1])] - Roman[Roman.index(s[i])]
                i += 2
            else:
                res += Roman[Roman.index(s[i])]
        return res

s = 'MCMXCIV'
print(Solution().romanToInt(s))
```

### Problem with the Code
The code fails with a `ValueError` because the `Roman` list contains integers, while the input string `s` contains characters.

---

## Transition to a Dictionary (Hashmap)
Using a dictionary resolves the issue by mapping Roman numeral characters directly to their integer values:

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = 0

        for i in range(len(s)):
            if i < (len(s) - 1) and Roman[s[i]] < Roman[s[i + 1]]:
                res += Roman[s[i + 1]] - Roman[s[i]]
                i += 2
            else:
                res += Roman[s[i]]
                i += 1
        return res

s = 'MCMXCIV'
print(Solution().romanToInt(s))
```

### Issue with the Above Code
Using `i += 2` within a `for` loop causes logical errors since the `for` loop automatically increments `i`. This leads to missed characters or incorrect calculations.

---

## Final Optimized Solution
The final version replaces the `for` loop with a `while` loop to correctly handle index increments:

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = 0
        i = 0

        while i < len(s):
            if i < (len(s) - 1) and Roman[s[i]] < Roman[s[i + 1]]:
                res += Roman[s[i + 1]] - Roman[s[i]]
                i += 2
            else:
                res += Roman[s[i]]
                i += 1
        return res

# Time complexity: O(n)
# Space complexity: O(1)

s = 'MCMXCIV'
print(Solution().romanToInt(s))
```

### Explanation
- **Dictionary (Hashmap):** Provides constant-time access to Roman numeral values.
- **While Loop:** Handles index increments dynamically without skipping characters.
- **Optimized Complexity:** The solution runs in linear time, `O(n)`, and uses constant space, `O(1)`.

---

## Example Output
For the input `s = 'MCMXCIV'`, the output is:
```plaintext
1994
```

---

This progression demonstrates the thought process and iterative improvements made to achieve a robust and efficient Roman numeral to integer converter.

