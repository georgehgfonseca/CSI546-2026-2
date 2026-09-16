# https://neetcode.io/problems/two-integer-sum/question

class Solution:
    # Time: O(n) Space: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complement = dict()
        for i in range(len(nums)):
            if nums[i] in complement:
                return [complement[nums[i]], i]
            diff = target - nums[i]
            complement[diff] = i

    # Time: O(n^2) Space: O(1)
    def twoSumBruteForce(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

testCases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1])
]

s = Solution()
passed = 0
for nums, target, expected in testCases:
    result = s.twoSum(nums, target)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")