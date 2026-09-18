# https://neetcode.io/problems/validate-parentheses/question

class Solution:
    # Time: O(n) Space: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in {"(", "[", "{"}:
                stack.append(char)
                continue

            if not stack:
                return False
            
            if stack[-1] == "(" and char != ")" or stack[-1] == "[" and char != "]" or stack[-1] == "{" and char != "}":
                return False

            stack.pop()

        return len(stack) == 0

    # Time: O(n) Space: O(n) 
    def isValidBruteForce(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''


testCases = [
    ("()[]{}", True),
    ("([)]", False),
    ("((()))", True)
]

s = Solution()
passed = 0
for s_input, expected in testCases:
    result = s.isValid(s_input)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")