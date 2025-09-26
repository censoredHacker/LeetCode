# Problem Name: Find All K-Distant Indices in an Array
# Problem Link: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
# Difficulty: Easy
# Tags: Array, Two Pointers

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:




if __name__ == "__main__":
    # Test cases
    sol = Solution()
    print(sol.findKDistantIndices([3, 4, 9, 1, 3, 9, 5], 2, 3))  # [0, 1, 2, 3, 4, 5, 6]
    print(sol.findKDistantIndices([2, 2, 2, 2, 2], 2, 2))  # [0, 1, 2, 3, 4]
    print(sol.findKDistantIndices([10, 9, 8], 1, 100))     # [0, 1, 2]