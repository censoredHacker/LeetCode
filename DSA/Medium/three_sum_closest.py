class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        arr = [-100000000]*3

        nums = sorted(nums)

        for i in range(0, len(nums)):
            current_diff = abs(target - (arr[0] + arr[1] + arr[2])) # 1
            
            diff_0 = abs(target - (nums[i] + arr[1] + arr[2])) # 2
            diff_1 = abs(target - (arr[0] + nums[i] + arr[2])) 
            diff_2 = abs(target - (arr[0] + arr[1] + nums[i]))


            if(diff_0 <= min(current_diff, diff_0, diff_1, diff_2)):
                arr[0] = nums[i]
            elif(diff_1 <= min(current_diff, diff_0, diff_1, diff_2)):
                arr[1] = nums[i]
            elif(diff_2 <= min(current_diff, diff_0, diff_1, diff_2)):
                arr[2] = nums[i]
        
        print(arr[0], arr[1], arr[2])
        return arr[0] + arr[1] + arr[2]
    


if __name__ == "__main__":
    solution = Solution()
    nums = [-84,92,26,19,-7,9,42,-51,8,30,-100,-13,-38]
    target = 78
    result = solution.threeSumClosest(nums, target)
    print(result)

    # -7 92 -13
    # 72
    # 9, 26, 42

            

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if abs(target - curr) < abs(target - closest):
                    closest = curr
                    
                if curr < target:
                    left += 1
                elif curr > target:
                    right -= 1
                else:
                    return target
        return closest