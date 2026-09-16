# https://neetcode.io/problems/duplicate-integer/question

class Solution:
    # Time: O(n) Space: O(n)
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        
        return False

    # Time: O(n^2) Space: O(1)
    def hasDuplicateBruteForce(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False

    
testCases = [
    ([1, 2, 3, 4], False),
    ([1, 2, 3, 2], True),
    ([1], False)
]

s = Solution()
passed = 0
for nums, expected in testCases:
    result = s.hasDuplicate(nums)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")