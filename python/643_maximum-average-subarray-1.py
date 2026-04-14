class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = len(nums)

        if k == 0 or l < k:
            return 0.0

        sum = 0

        for i in range(0, k):
            sum += nums[i]

        max_avg = sum / k

        for i in range(k, l):
            sum -= nums[i - k]
            sum += nums[i]
            max_avg = max(max_avg, sum / k)

        return max_avg


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert solution.findMaxAverage([5], 1) == 5.0
