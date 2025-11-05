# Problem: 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(0, len(haystack)):
            sub = haystack[i, i + len(needle)]
            if sub == needle:
                return i 
            
        return -1