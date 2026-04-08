class Solution:
    
    def climbStairs(self, n: int) -> int:
        memo = {}
        def calcSteps(s: int):
            if s == 1:
                return 1
            if s == 2:
                return 2
            if s in memo:
                return memo[s]

            memo[s] = calcSteps(s-1)  + calcSteps(s-2)
            return memo[s]
        return calcSteps(n)