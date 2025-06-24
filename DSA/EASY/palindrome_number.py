# Problem Name: Palindrome Number
# Problem Link: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Tags: Math, String
class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = str(x)

        if(org == org[::-1]):
            return True

        return False 

    # Slower solution
    # def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        
        # if x < 10:
        #     return True
        
        # original = x
        # reverse = 0

        # while original > 9:
        #     reverse = reverse*10 + int(original%10)
        #     original = int(original/10)
        
        # reverse = reverse*10 + original
        
        # if reverse == x:
        #     return True
        
        # return False
     

if __name__ == "__main__":    # Example usage        solution = Solution()
        x = 12221
        solution = Solution()
        result = solution.isPalindrome(x)
        print(result)