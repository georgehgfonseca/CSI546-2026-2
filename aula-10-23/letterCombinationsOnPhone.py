# Backtracking, Hash Table
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        pass # todo: implement this function
    

testCases = [
    # output can be in any order
    ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
    ("2", ["a","b","c"]),
]

s = Solution()
passed = 0
for digits, expected in testCases:
    result = s.letterCombinations(digits)
    assert {tuple(x) for x in result} == {tuple(x) for x in expected}, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")