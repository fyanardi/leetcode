import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        merged = sorted(list(zip(nums1, nums2)), key=lambda x: x[1], reverse=True)
        # store num1 values that correspond to num2 that has been processed
        # in a Priority Queue structure, the smallest of the 
        heap = []
        max_score = 0
        sum = 0

        for num1, num2 in merged:
            heapq.heappush(heap, num1)
            sum += num1

            if len(heap) > k:
                # subtract sum by the smallest of num1 in the heap since we want to maximize the
                # sum of num1
                sum -= heapq.heappop(heap)
            if len(heap) == k:
                max_score = max(max_score, num2 * sum)

        return max_score


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxScore(nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3) == 12
    assert solution.maxScore(nums1=[4, 2, 3, 1, 1], nums2=[7, 5, 10, 9, 6], k=1) == 30
    assert solution.maxScore(nums1=[1, 4], nums2=[3, 1], k=2) == 5
    assert solution.maxScore(nums1=[2, 1, 14, 12], nums2=[11, 7, 13, 6], k=3) == 168
