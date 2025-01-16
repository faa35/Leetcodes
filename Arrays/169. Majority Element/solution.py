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

        # swapping nums elements with results elements
        for i in range(len(nums)):
            nums[i] = result[i]

# Example usage
nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
