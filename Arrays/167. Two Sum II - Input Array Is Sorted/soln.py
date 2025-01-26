class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
#         for i in range(len(numbers)):
#             for j in range(i+1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i+1,j+1]
                

# numbers = [2,7,11,15]
# target = 9
# sol = Solution()
# print(sol.twoSum(numbers, target)) #[1,2]











        # s = set()
        # for i in range(len(numbers)):
        #     if target - numbers[i] in s:
#--------hobena cause amader index o return kora lagbe 
#--------so its gonna be HASHMAP

        s = {}

        result = []

        for i in range(len(numbers)):
            if (target - numbers[i]) in s:

                #type 1
                result.append(s[target - numbers[i]] + 1)
                result.append(i+1)
                return result

                # #type 2(without the list RESULT)
                # return [(s[target - numbers[i]] + 1), (i+1)]

            else:
                s[numbers[i]] = i 