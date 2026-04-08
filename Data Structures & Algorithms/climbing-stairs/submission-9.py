class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def countWays(step: int):
            if step <= 2:
                return step
            if step in memo:
                return memo[step]
            memo[step] = countWays(step - 1) + countWays(step - 2)
            return memo[step]
        return countWays(n)
