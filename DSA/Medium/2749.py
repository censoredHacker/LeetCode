

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        for i in range(0,61):
            if num1 - i * num2 < 0:
                return -1
            if bin(num1 - i * num2).count('1') <= i:
                return i


