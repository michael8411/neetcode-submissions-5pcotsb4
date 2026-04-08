class Solution:
    def climbStairs(self, n: int) -> int:
        ways_memo = {}

        def ways(steps: int) -> int:
            """Return number of ways to climb exactly `steps` steps."""
            if steps <= 2:
                return steps

            if steps in ways_memo:
                return ways_memo[steps]

            ways_memo[steps] = ways(steps - 1) + ways(steps - 2)
            return ways_memo[steps]

        return ways(n)
