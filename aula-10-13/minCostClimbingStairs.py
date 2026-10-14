# Dynamic Programming
# https://neetcode.io/problems/climb-stairs/question

from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        
        @cache
        def dfs(i):
            if i >= len(cost):
                return 0
            
            return cost[i] + min(dfs(i + 1), dfs(i + 2))

        return min(dfs(0), dfs(1))


testCases = [
    ([1, 2, 3], 2),
    ([1, 2, 1, 2, 1, 1, 1], 4),
]

s = Solution()
passed = 0
for nums, expected in testCases:
    result = s.minCostClimbingStairs(nums)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")