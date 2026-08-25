class Solution:
    def numTilings(self, n):
        MOD = 10**9 + 7

        if n == 1:
            return 1
        if n == 2:
            return 2

        a, b, c = 1, 2, 5

        for _ in range(4, n + 1):
            a, b, c = b, c, (2 * c + a) % MOD

        return c