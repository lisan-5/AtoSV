class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime_factors(x):
            factors = set()
            while x % 2 == 0:
                factors.add(2)
                x //= 2
            for i in range(3, int(x**0.5) + 1, 2):
                while x % i == 0:
                    factors.add(i)
                    x //= i
            if x > 2:
                factors.add(x)
            return factors

        result = set()
        for num in nums:
            result.update(prime_factors(num))
        
        return len(result)
