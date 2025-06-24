# Problem Name: Valid Parentheses
# Problem Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Tags: Stack, String

# Beats 100%
def isValid(s: str) -> bool:
    stack = []
    close_paranthese = {'}', ']', ')'}
    for char in s:
        if char in close_paranthese:
            if not stack:
                return False
            top = stack.pop()
            if (top+char) == '{}' or (top+char) == '()' or (top+char) == '[]' :
                continue
            else: 
                return False
        else: 
            stack.append(char)

    if not stack:
        return True
    
    return False


if __name__ == "__main__":    # Test cases
    print(isValid("()"))          # True
    print(isValid("((([[{[]}]])))"))      
    print(isValid("(]"))