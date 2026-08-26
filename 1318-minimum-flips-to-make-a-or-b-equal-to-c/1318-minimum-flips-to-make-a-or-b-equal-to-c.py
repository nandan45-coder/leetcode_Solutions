class Solution:
    def minFlips(self, a, b, c):
        ans = 0

        while a or b or c:
            bitA = a & 1
            bitB = b & 1
            bitC = c & 1

            if bitC == 1:
                if bitA == 0 and bitB == 0:
                    ans += 1
            else:
                ans += bitA + bitB

            a >>= 1
            b >>= 1
            c >>= 1

        return ans