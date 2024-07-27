class Solution:
    def minSteps(self, n: int) -> int:
        steps = 0
        i = 2
        while i * i <= n:
            if n % i == 0:
                steps += i
                n //= i
            else:
                i += 1
        if n > 1:
            steps += n
        return steps
