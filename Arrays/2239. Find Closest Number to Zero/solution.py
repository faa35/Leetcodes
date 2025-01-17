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

        if closest<0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest



soluion = Solution()
print(soluion.findClosestNumber([1, 2, 3, -4])) 