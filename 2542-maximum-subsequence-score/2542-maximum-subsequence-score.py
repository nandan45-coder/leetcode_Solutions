import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        pairs = list(zip(nums2, nums1))
        pairs.sort(reverse=True)

        min_heap = []
        total = 0
        answer = 0

        for num2, num1 in pairs:
            heapq.heappush(min_heap, num1)
            total += num1

            if len(min_heap) > k:
                total -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                answer = max(answer, total * num2)

        return answer