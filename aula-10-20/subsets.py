# Backtracking
# https://neetcode.io/problems/subsets/question

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res, n = [], len(nums)

        def dfs(i, curr):
            if i >= n:
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1, curr)

        dfs(0, [])
        return res
    

testCases = [
    # output can be in any order
    ([1,2,3], [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]),
]

s = Solution()
passed = 0
for nums, expected in testCases:
    result = s.subsets(nums)
    assert {tuple(x) for x in result} == {tuple(x) for x in expected}, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")