class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def countSteps(step):
            if step <= 2:
                return step
            if step in memo:
                return memo[step]
            memo[step] = countSteps(step - 1) + countSteps(step - 2)
            return memo[step]
        return countSteps(n)

