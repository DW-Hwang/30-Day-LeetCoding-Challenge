"""
*.*.*.*.*.*
Given a string containing only three types of characters:
 '(' ,  ')'  and  '*' , write a function to check whether
this string is valid. We define the validity of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
5. An empty string is also valid.

Note:
The string size will be in the range [1, 100].
*.*.*.*.*.*

# Example 1:
Input: "()"
Output: True

# Example 2:
Input: "(*)"
Output: True

# Example 3:
Input: "(*))"
Output: True
"""

class Solution1:
    def checkValidString(self, s):
        hi, lo = 0, 0
        for par in s:
            lo += 1 if par == '(' else -1
            hi += 1 if par != ')' else -1
            
            if (hi < 0):
                break
            
            lo = max(lo, 0)
        
        return lo == 0


# Alternatively
class Solution2:
    def checkValidString(self, s):
        stack = []
        star_stack = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            
            elif s[i] == '*':
                star_stack.append(i)
            
            else:
                if not stack and not star_stack:
                    return False
                if stack:
                    stack.pop()
                else:
                    star_stack.pop()
        
        while stack and star_stack:
            
            if stack.pop()>star_stack.pop():
                return False
        
        return not stack
        

if __name__ == "__main__":
    
    print '(Solution 1) Execute input s = "()" :: ', Solution1().checkValidString("()")
    print '(Solution 1) Execute input s = "(*)" :: ', Solution1().checkValidString("(*)")
    print '(Solution 1) Execute input s = "(*))" :: ', Solution1().checkValidString("(*))")

    print '(Solution 2) Execute input s = "()" :: ', Solution2().checkValidString("()")
    print '(Solution 2) Execute input s = "(*)" :: ', Solution2().checkValidString("(*)")
    print '(Solution 2) Execute input s = "(*))" :: ', Solution2().checkValidString("(*))")


	
