import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)

        if 2 * candidates >= n:
            return sum(heapq.nsmallest(k, costs))

        left = []
        right = []

        # First candidates workers
        for i in range(candidates):
            heapq.heappush(left, (costs[i], i))

        # Last candidates workers
        for i in range(n - candidates, n):
            heapq.heappush(right, (costs[i], i))

        l = candidates
        r = n - candidates - 1
        total = 0

        for _ in range(k):
            # Choose lower cost; if equal, smaller index
            if left and right:
                if left[0] <= right[0]:
                    cost, idx = heapq.heappop(left)

                    if l <= r:
                        heapq.heappush(left, (costs[l], l))
                        l += 1
                else:
                    cost, idx = heapq.heappop(right)

                    if l <= r:
                        heapq.heappush(right, (costs[r], r))
                        r -= 1

            elif left:
                cost, idx = heapq.heappop(left)
            else:
                cost, idx = heapq.heappop(right)

            total += cost

        return total