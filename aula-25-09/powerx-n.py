# Math Divide-and-Conquer
# https://leetcode.com/problems/powx-n/

class Solution:
    # Time: O(n) Space: O(n)
    def myPowBruteForce(self, x: float, n: int) -> float:
        if n == 1:
            return x
        return x * self.myPowBruteForce(x, n - 1)

    # Time O(log n) Space: O(log n)
    def myPow(self, x, n):
        if n == 1:
            return x
        y = self.myPow(x, n // 2)

        if n % 2 == 0:
            return y * y
        else:
            return x * y * y