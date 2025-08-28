# Problem Name: Remove Element
# Problem Link: https://leetcode.com/problems/remove-element/description/
# Difficulty: Easy

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        result = 0

        for i in range(len(nums)):

            if nums[i] != val:
                result = i
            if nums[i] == val:
                
                for j in range(i+1, len(nums)):
                    if nums[j] != val:
                        nums[i] = nums[j]
                        nums[j] = val
                        result = i
                        i = j
                        break
        return result+1
    
    # By IDOR:
    # if nums[i] != val:
    #     nums[k] = nums[i] 
    #     k += 1 
    #     return k
    
if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,2,3]
    val = 3
    result = solution.removeElement(nums, val)
    print(result, nums)