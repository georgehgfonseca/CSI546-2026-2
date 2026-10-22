# Backtracking
# https://neetcode.io/problems/combination-target-sum/question

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
    

testCases = [
    # output can be in any order
    ([2,5,6,9], 9, [[2,2,5],[9]]),
    ([3,4,5], 16, [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]),
]

s = Solution()
passed = 0
for nums, target, expected in testCases:
    result = s.combinationSum(nums, target)
    assert {tuple(x) for x in result} == {tuple(x) for x in expected}, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")