# Problem Name: Remove Duplicates from Sorted Array
# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Difficulty: Easy


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums) 

        count = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]: 
                nums[count] = nums[i]
                count += 1
            
        return count
    

if __name__ == "__main__":    # Example usage
    solution = Solution()
    nums = [0,1,1,2,2,3]
    result = solution.removeDuplicates(nums)
    print(result, nums)
