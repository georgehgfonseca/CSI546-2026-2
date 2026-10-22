# Dynamic Programming
# https://neetcode.io/problems/house-robber/question

from functools import cache

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        
        @cache
        def dfs(i, robbed):
            if i >= n:
                return 0

            if robbed:
                return nums[i] + dfs(i + 1, False)
                        
            return max(dfs(i + 1, False), dfs(i + 1, True))
        
        return max(dfs(0, True), dfs(0, False))
    

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