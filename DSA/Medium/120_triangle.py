# Problem: 120. Triangle
# Difficulty: Medium

class Solution:


    def minimumTotal(self, triangle: list[list[int]]) -> int:
        total = 0
        dp = []


        for row in range(len(triangle)-1, -1, -1) :

            # Base case
            # If we are at the last row, we just take the values as they are
            if row == len(triangle) - 1:
                dp = triangle[row]
                continue

            # Intermediate case
            for index in range(len(triangle[row])):
                dp[index] = triangle[row][index] + min(dp[index], dp[index + 1])

            # Final case
            # The first element of the dp array will have the minimum path sum
            if row == 0:
                return dp[0]

if __name__ == "__main__" :
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(Solution().minimumTotal(triangle))