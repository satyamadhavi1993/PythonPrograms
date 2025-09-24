# Given an integer n, return the number of prime numbers that are strictly less than n.


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        p = 2
        
        while p * p < n:
            if primes[p]:
                for value in range(p*p, n, p):
                    primes[value] = False
            p += 1
        
        return sum(primes)

sol = Solution()
print(sol.countPrimes(10))