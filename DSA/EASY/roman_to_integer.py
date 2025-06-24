# Problem Name: Roman to Integer
# Problem Link: https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy
# Tags: Hash Table, Math, String

        
# Beats 87%
class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for i in range(len(s)):
            if i < (len(s) - 1) and (roman_numerals[s[i]] < roman_numerals[s[i+1]]):
                result -= roman_numerals[s[i]]
                continue
            
            result += roman_numerals[s[i]]

        return result

# Slower solution: Beats 15%
# class Solution:
#     def romanToInt(self, s: str) -> int:
        
#         roman_numerals = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
        
#         sub_set = {'I', 'X', 'C'}

#         result = 0

#         for i in range(len(s)):
#             if s[i] in sub_set and i < (len(s) - 1) and (roman_numerals[s[i]] < roman_numerals[s[i+1]]):
#                 result -= roman_numerals[s[i]]
#                 continue
            
#             result += roman_numerals[s[i]]

#         return result




if __name__ == "__main__":
    solution = Solution()        
    s = "MCMXCIV"
    result = solution.romanToInt(s)
    print(result)