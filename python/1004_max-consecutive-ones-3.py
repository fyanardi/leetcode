class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)

        left = 0
        right = 0
        zeroes = 0
        max_ones = 0

        while right < n:
            if nums[right] == 1:
                right += 1
            else:
                if zeroes == k:
                    max_ones = max(max_ones, right - left)
                    # skip all leading 1s
                    while left <= right and nums[left] != 0:
                        left += 1
                    # skip the first zero
                    left += 1
                    zeroes -= 1
                else:
                    zeroes += 1
                    right += 1

        # in case the last digit processed is 1 or number of zeroes is still less than k
        return max(max_ones, right - left)


if __name__ == "__main__":
    solution = Solution()

    assert solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2) == 6
    assert solution.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3) == 10
    assert solution.longestOnes(nums=[0, 0, 0, 1], k=4) == 4
