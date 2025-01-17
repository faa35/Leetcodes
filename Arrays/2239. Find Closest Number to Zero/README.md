# [2239. Find Closest Number to Zero](https://leetcode.com/problems/find-closest-number-to-zero/)

## Problem Statement

Given an integer array `nums` of size `n`, return the number with the value closest to `0` in `nums`. If there are multiple answers, return the number with the **largest value**.

---

### Example

#### Example 1:
**Input:**  
`nums = [-4, -2, 1, 4, 8]`  
**Output:**  
`1`  
**Explanation:**  
- The distance from -4 to 0 is 4.  
- The distance from -2 to 0 is 2.  
- The distance from 1 to 0 is 1.  
- The distance from 4 to 0 is 4.  
- The distance from 8 to 0 is 8.  

Thus, the closest number to 0 in the array is `1`.

---

#### Example 2:
**Input:**  
`nums = [2, -1, 1]`  
**Output:**  
`1`  
**Explanation:**  
`1` and `-1` are both the closest numbers to `0`, but `1` (being larger) is returned.

---

### Constraints:
- \(1 \leq n \leq 1000\)
- \(-10^5 \leq nums[i] \leq 10^5\)

---

## Solution

### Approach

**Intuition:**

To find the number closest to zero, iterate through the array while maintaining a variable `closest` that tracks the number with the smallest absolute value. If two numbers have the same absolute value, the positive number should be preferred.

**Steps:**
1. Start with `closest` as the first number in the array.
2. Iterate through the array:
   - Compare the absolute value of each number with the absolute value of `closest`.
   - Update `closest` if the current number has a smaller absolute value.
3. After the loop, check if `closest` is negative and its positive counterpart exists in the array. If so, return the positive value; otherwise, return `closest`.

**Code:**

```python
class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = nums[0]

        for i in range(len(nums)):
            if abs(closest) > abs(nums[i]):
                closest = nums[i]

        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
```

**Complexity Analysis:**
- **Time Complexity:** \(O(n)\), since we iterate through the array once.  
- **Space Complexity:** \(O(1)\), as no additional space is used.

---

### Example Usage:

```python
nums = [-4, -2, 1, 4, 8]
print(Solution().findClosestNumber(nums))  # Output: 1

nums = [2, -1, 1]
print(Solution().findClosestNumber(nums))  # Output: 1
```

The approach ensures that the closest number to zero is correctly identified, handling tie cases effectively by preferring the positive number when absolute values are equal.
