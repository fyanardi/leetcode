class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        # [l, r] is the window of possible positions of every jump, every position in the window
        # needs to be considered to derive the next window
        l = r = 0

        while r < len(nums) - 1:
            # within this window, what's the farthest we can go
            farthest = 0

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            # we've jumped and define next window to evaluate
            jumps += 1
            l = r + 1
            r = farthest

        return jumps


if __name__ == "__main__":
    solution = Solution()
    assert solution.jump([2,3,1,1,4]) == 2
    assert solution.jump([2,3,0,1,4]) == 2
    assert solution.jump([1,3,5,8,9,2,6,7,6,8,9]) == 3
    assert solution.jump([1,4,3,2,6,7]) == 2
