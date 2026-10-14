# Dynamic Programming
# https://neetcode.io/problems/climb-stairs/question

from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == n:
                return 1
            if i > n:
                return 0

            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)

    def climbStairsCache(self, n: int) -> int:
        cache = {}
        
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == n:
                return 1
            if i > n:
                return 0

            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)


testCases = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8)
]

s = Solution()
passed = 0
for nums, expected in testCases:
    result = s.climbStairs(nums)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")