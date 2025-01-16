# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

## Approaches
1. [Naive Approach - Using Additional Array](#naive-approach)
2. [Optimal Approach - Two Pointer Technique](#optimal-approach)

### Naive Approach - Using Additional Array

**Intuition:**

This approach leverages the use of an additional array to store the non-zero elements separately and finally concatenate the zeroes with the non-zero elements array. The idea is to iterate through the original array and build a separate list of non-zero elements. Once gathered, we'll fill the rest of the original array with zeroes.

**Steps:**

1. Initialize an empty list `result` to store non-zero elements.
2. Iterate over each element `num` in the array `nums`.
3. If `num` is non-zero, append it to the `result` list.
4. Calculate the number of zeroes `zero_count` by subtracting the length of `result` from the length of `nums`.
5. Extend `result` by the list of zeroes `[0] * zero_count`.
6. Replace `nums` elements with elements from `result` to achieve in-place requirement.

**Code:**

```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        result = []
        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(nums[i])
        zero_count = len(nums) - len(result)
        result.extend([0] * zero_count)

        for i in range(len(nums)):
            nums[i] = result[i]

# Example usage
nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
```

**Complexity Analysis:**

- **Time Complexity:** \(O(n)\), where \(n\) is the number of elements in the list because we iterate through the list twice.
- **Space Complexity:** \(O(n)\), since we are using an additional list `result` to store the non-zero elements.

### Optimal Approach - Two Pointer Technique

**Intuition:**

This approach improves upon the naive approach by eliminating the need for an auxiliary list. Instead, we rearrange the elements in-place using a two-pointer technique. We maintain one pointer, `non_zero`, to track the position of the last non-zero element. As we iterate, we swap non-zero elements with the position pointed by `non_zero`.

**Steps:**

1. Initialize a pointer `non_zero` at index 0.
2. Iterate through each element in `nums` using a pointer `i`.
3. If the current element `nums[i]` is non-zero, swap `nums[i]` with `nums[non_zero]`.
4. Increment `non_zero` after the swap to move to the next position.
5. Post iteration, all non-zero elements are at the beginning and rest are zeroes.

**Code:**

```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1

# Example usage
nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
```

**Complexity Analysis:**

- **Time Complexity:** \(O(n)\), since we pass through the array exactly once besides the constant-time swaps.
- **Space Complexity:** \(O(1)\), no additional list is used, thus achieving in-place rearrangement.

By using the two-pointer technique, we achieve an optimal solution that is both time-efficient and space-efficient, making it suitable for scenarios with space constraints.
