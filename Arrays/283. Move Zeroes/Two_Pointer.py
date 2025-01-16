class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:      # if nums[i]:    # if the element is not zero then do (the below operation)
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1

# Example usage
nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
