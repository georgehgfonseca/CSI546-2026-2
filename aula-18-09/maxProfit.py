# https://neetcode.io/problems/buy-and-sell-crypto/question

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pass

testCases = [
    ([10, 1, 5, 6, 7, 1], 6),
    ([3, 2, 4], 2),
    ([3, 3], 0)
]

s = Solution()
passed = 0
for prices, expected in testCases:
    result = s.maxProfit(prices)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")