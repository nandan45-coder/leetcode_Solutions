class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1

            if partition1 == 0:
                max_left1 = float('-inf')
            else:
                max_left1 = nums1[partition1 - 1]

            if partition1 == m:
                min_right1 = float('inf')
            else:
                min_right1 = nums1[partition1]

            if partition2 == 0:
                max_left2 = float('-inf')
            else:
                max_left2 = nums2[partition2 - 1]

            if partition2 == n:
                min_right2 = float('inf')
            else:
                min_right2 = nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))

                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0

            if max_left1 > min_right2:
                high = partition1 - 1
            else:
                low = partition1 + 1

        return 0.0