"""
Given a string s that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any bracket.

Example 1:

Input: s = "(abcd)"
Output: "dcba"
"""

def reverseParentheses(s: str) -> str:
    if '(' not in s: 
        return s
    open=s.rindex('(')
    close=s[open:].index(')')+open
    a=s[0:open]
    b=s[open+1:close][::-1]
    c=s[min(close+1, len(s)):len(s)]
    return reverseParentheses(a+b+c)

input=["(u(love)i)", "(ed(et(oc))el)", "a(bcdefghijkl(mno)p)q"]
expected=["iloveu", "leetcode", "apmnolkjihgfedcbq"]
output=[reverseParentheses(i) for i in input]
print(input)
print(expected)
print(output)