# https://neetcode.io/problems/meeting-schedule/question

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        pass

testCases = [
    ([Interval(0, 30), Interval(5, 10), Interval(15, 20)], False),
    ([Interval(5, 8), Interval(9, 15)], True),
]

s = Solution()
passed = 0
for intervals, expected in testCases:
    result = s.canAttendMeetings(intervals)
    assert result == expected, f"Expected {expected}, but got {result}"
    passed += 1

print(f"Passed: {passed}/{len(testCases)}")