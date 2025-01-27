class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # print(min(height[0],height[8]))

        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         y = min(height[i],height[j])
        #         x = j-i
        #         area = x*y

        #         if area > max_area:
        #             max_area = area
        # return max_area




        max_area = 0

        i = 0
        j = len(height) - 1

        while j > i:
            y = min(height[i],height[j])
            x = j-i

            area = x*y

            if area > max_area:
                max_area = area
            
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else: # height[i] == height[j]
            # really doesn't matter
            # we can update any pointer
                i += 1

        return max_area


sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height)) #49


