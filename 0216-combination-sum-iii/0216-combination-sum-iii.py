class Solution:
    def combinationSum3(self, k, n):
        result = []

        def backtrack(start, current, total):
            if len(current) == k:
                if total == n:
                    result.append(current[:])
                return

            if total >= n:
                return

            for i in range(start, 10):
                current.append(i)
                backtrack(i + 1, current, total + i)
                current.pop()

        backtrack(1, [], 0)
        return result