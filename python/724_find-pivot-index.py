class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        right = 0

        for i in range(0, len(nums) - 1):
            right += nums[i + 1]

        if left == right:
            return 0

        for j in range(1, len(nums)):
            left += nums[j - 1]
            right -= nums[j]

            if left == right:
                return j

        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert solution.pivotIndex([1, 2, 6]) == -1
    assert solution.pivotIndex([2, 1, -1]) == 0
    assert solution.pivotIndex([3]) == 0
