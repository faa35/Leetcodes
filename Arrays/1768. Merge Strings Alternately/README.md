# Merge Strings Alternately

This repository contains a Python implementation of the LeetCode problem "Merge Strings Alternately." The goal is to merge two strings alternately by adding characters from each string in sequence. If one string is longer than the other, the remaining characters are appended to the result.

## Problem Description

**Input:**
- Two strings `word1` and `word2`, consisting of lowercase English letters.

**Output:**
- A single string where characters from `word1` and `word2` are merged alternately. Any leftover characters from the longer string are appended at the end.

### Example

**Example 1:**
```text
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
```

**Example 2:**
```text
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
```

**Example 3:**
```text
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
```

### Constraints
- `1 <= word1.length, word2.length <= 100`
- `word1` and `word2` consist of lowercase English letters.

## Code Implementation
```python
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
```

## Complexity Analysis

### Time Complexity
- **O(n + m):**
  - Where `n` is the total length of the strings (`word1`).
  - and, `m` is the total length of the strings (`word2`).

### Space Complexity
- **O(n + m):**             **?**
  - Additional space is used to store the result string, which grows proportionally with the combined length of the input strings.




