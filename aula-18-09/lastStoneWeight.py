# https://neetcode.io/problems/last-stone-weight/question

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        pass

testCases = [
    ([2, 3, 6, 2, 4], 1),
    ([1, 2], 1),
    ([3, 3], 0)
]

s = Solution()
passed = 0
for stones, expected in testCases:
    result = s.lastStoneWeight(stones)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")