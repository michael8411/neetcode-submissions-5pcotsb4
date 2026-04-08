class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 1]
        for i in range(n):
            if i == n - 1:
                return steps[i+1]
            s1 = steps[i]
            s2 = steps[i+1]
            steps.append(s1 + s2)

       
       
       
       
       
       
       
       
       
        # memo = {}
        # def countSteps(step):
        #     if step <= 2:
        #         return step
        #     if step in memo:
        #         return memo[step]
        #     memo[step] = countSteps(step - 1) + countSteps(step - 2)
        #     return memo[step]
        # return countSteps(n)

