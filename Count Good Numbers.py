class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def power(x, y, p):
            res = 1
            x = x % p
            while y > 0:
                if (y & 1) == 1:
                    res = (res * x) % p
                y = y >> 1
                x = (x * x) % p
            return res
        
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        
        return (power(5, even_positions, MOD) * power(4, odd_positions, MOD)) % MOD
