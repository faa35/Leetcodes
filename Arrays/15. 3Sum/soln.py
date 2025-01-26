class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # #1
        # print(sorted(nums))  #[-4, -1, -1, 0, 1, 2]

        # #2
        # nums.sort()
        # print(nums)  #[-4, -1, -1, 0, 1, 2]




        nums.sort()

        result=[]

        for i in range(len(nums)):
            

            if i>0 and nums[i-1] == nums[i]:
                continue
            
            j = i+1
            k = len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    result.append([nums[i],nums[j],nums[k]])

                    j += 1
                    k -= 1

                    while nums[j] == nums[j-1] and j<k:
                        j+=1
    
                
        return result
    
nums = [-1, 0, 1, 2, -1, -4]

sol = Solution()
print(sol.threeSum(nums)) #[[-1, -1, 2], [-1, 0, 1]]