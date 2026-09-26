# https://leetcode.com/problems/fibonacci-number/description

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

testCases = [
    (2, 1),
    (3, 2),
    (4, 3),
]

s = Solution()
passed = 0
for n, expected in testCases:
    result = s.fib(n)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")