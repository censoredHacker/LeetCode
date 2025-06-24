# Problem Name: Longest Common Prefix
# Problem Link: https://leetcode.com/problems/longest-common-prefix/
# Problem Difficulty: Easy
# Tags: String, Array, Divide and Conquer

class Solution:
    # Beats 100%
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        # find smallest string
        smallest = min(strs, key=len)
        flag = True

        for i in range(len(smallest)):
            for item in strs:
                if smallest[i] == item[i]:
                    continue
                else:
                    flag = False
                    break
            
            if flag == False:
                break

            prefix += smallest[i]

        return prefix
        


if __name__ == "__main__":    # Example usage
    solution = Solution()
    strs = ["flower","flow","flight"]
    result = solution.twoSum(strs)
    print(result)