# Problem Name: Two Sum
# Problem Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Tags: Array, Hash Table, Two Pointers

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            try:
                pair = nums.index(target-nums[i])
                if pair >= 0:        
                    return [i,pair]
                
            except:
                pass

# Slower solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if(nums[i] + nums[j] == target):
#                     return [i,j]


if __name__ == "__main__":    # Example usage
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 17
    result = solution.twoSum(nums, target)
    print(result)