class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(x):
            if x < 2:
                return False
            if x in (2, 3):
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True

        primes = [i for i in range(left, right + 1) if is_prime(i)]
        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        result = [-1, -1]
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                result = [primes[i], primes[i + 1]]
        
        return result
