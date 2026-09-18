# https://neetcode.io/problems/buy-and-sell-crypto/question

class Solution:
    # Time: O(n) Space: O(1)
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        lowest = prices[0]
        for i in range(len(prices)):
            if prices[i] > lowest:
                profit = max(profit, prices[i] - lowest)
            else:
                lowest = prices[i]

        return profit

    # Time: O(n^2) Space: O(1)
    def maxProfitBruteForce(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        return max_profit

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