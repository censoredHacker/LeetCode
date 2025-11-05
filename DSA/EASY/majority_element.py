class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}

        threshold = int(len(nums)/2)

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1 #update frequency 
                if hash_map.get(num) > threshold:
                    return num
            else:
                hash_map[num] = 1
        
        return -1