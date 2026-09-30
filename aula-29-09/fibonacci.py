# Dynamic Programming
# https://leetcode.com/problems/fibonacci-number/description

from functools import cache

class Solution:
    def fib(self, n: int) -> int:
        # Top-down approach with memoization Time: O(n) Space: O(n)
        cache = {}

        def dfs(n):
            if n in cache:
                return cache[n]
            if n == 0 or n == 1:
                return n
            cache[n] = dfs(n - 1) + dfs(n - 2)
            return cache[n]

        return dfs(n)

    def fibV2(self, n: int) -> int:
        # Top-down approach cache annotation Time: O(n) Space: O(n)
        @cache
        def dfs(n):
            if n == 0 or n == 1:
                return n
            return dfs(n - 1) + dfs(n - 2)

        return dfs(n)

    def fibV3(self, n: int) -> int:
        # Bottom-up approach Time: O(n) Space: O(n)
        cache = [0, 1]
        for i in range(2, n + 1):
            cache.append(cache[i - 1] + cache[i - 2])
        return cache[n]

    def fibV4(self, n: int) -> int:
        # Bottom-up approach Time: O(n) Space: O(1)
        if n == 0 or n == 1:
            return n
        prev, prevPrev = 1, 0
        for _ in range(2, n + 1):
            prev, prevPrev = prev + prevPrev, prev
        return prev

testCases = [
    (5, 5),
    (6, 8),
    (7, 13),
]

s = Solution()
passed = 0
for n, expected in testCases:
    result = s.fibV4(n)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")