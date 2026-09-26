# Dynamic Programming
# https://neetcode.io/problems/house-robber/question

class Solution:
    def rob(self, nums: list[int]) -> int:
        pass

testCases = [
    ([1, 1, 3, 3], 4),
    ([2, 9, 8, 3, 6], 16)
]

s = Solution()
passed = 0
for nums, expected in testCases:
    result = s.rob(nums)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")