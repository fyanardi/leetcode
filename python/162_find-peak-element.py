class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        j = n - 1

        while j >= i:
            mid = (i + j) // 2
            gt_left = mid == 0 or nums[mid] > nums[mid-1]
            gt_right = mid == n - 1 or nums[mid] > nums[mid+1]
            # greater than both, means it's a peak
            if gt_left and gt_right:
                return mid
            elif not gt_left:
                # less than left, we move search space to the left
                # if the left is monotonically decreasing, the peak will be at index 0
                # otherwise it's also guaranteed to find a peak in the left
                j = mid - 1
            else:
                # Same logic with gt_right condition
                i = mid + 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.findPeakElement([1, 2, 3, 1]) == 2
    assert solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
