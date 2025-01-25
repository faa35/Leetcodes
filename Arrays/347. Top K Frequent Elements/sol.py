class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #type 1
        s = {}  # nums = [1,1,1,2,2,3]

        # Count the frequency of each element
        for i in range(len(nums)):  
            if nums[i] in s:
                s[nums[i]] += 1
            else:
                s[nums[i]] = 1

        # print(s) #{1: 3, 2: 2, 3: 1}


        # #type 2
        # import collections
        # s = collections.defaultdict(int)
        # print(s) #defaultdict(<type 'int'>, {})

        # # Count the frequency of each element
        # for num in nums:
        #     s[num] += 1  # Increment the count for the current number

        # print(s) #defaultdict(<type 'int'>, {1: 3, 2: 2, 3: 1})



        ### NOW WE ARE GOING THE INVERT THE KEY AND VALUE
        ###{1: 3, 2: 2, 3: 1} to {3: 1, 2: 2, 1: 3}

        my_heap = []  # REMEMBER a HEAP is an ARRAY not a hashmap
        for key, v in s.items():  # Iterate through the items in the dictionary
            my_heap.append((v, key))  # Append the tuple (v, k) to the list
        
        # print(my_heap) #[(3, 1), (2, 2), (1, 3)]


        ###NOW WE ARE GOING TO make this a real HEAP
        import heapq
        heapq.heapify(my_heap)  # This transforms the list into a valid MIN-heap
        # print(my_heap) #[(1, 3), (2, 2), (3, 1)]



        ###NOW WE ARE GONNA pop the min values
        ### meaning the least frequent value
        while len(my_heap) > k:
            heapq.heappop(my_heap)
        #print(my_heap) #[(2, 2), (3, 1)]

        result = []

        for key,v in my_heap:
            result.append(v)
        return result
        


solution = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(solution.topKFrequent(nums, k))  # Output: [2, 1]