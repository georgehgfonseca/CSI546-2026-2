# Giving a string of match results W, L, D, return the length of the longest winning streak (consecutive W's) in the string.

class Solution:
    # Time: O(n) Space: O(1)
    def longestWinningStreak(self, s: str) -> int:
        max_streak = 0 
        current_streak = 0

        for char in s:
            if char == "W":
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 0

        return max_streak

    
testCases = [
    ("WLW", 1),
    ("WWLWW", 2),
    ("LLL", 0)
]

s = Solution()
passed = 0
for s_input, expected in testCases:
    result = s.longestWinningStreak(s_input)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")