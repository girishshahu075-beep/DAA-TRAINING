class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            a = nums1[i-1] if i > 0 else float('-inf')
            b = nums1[i] if i < m else float('inf')
            c = nums2[j-1] if j > 0 else float('-inf')
            d = nums2[j] if j < n else float('inf')

            if a <= d and c <= b:
                if (m+n) % 2:
                    return max(a, c)
                return (max(a, c) + min(b, d)) / 2

            elif a > d:
                high = i - 1
            else:
                low = i + 1