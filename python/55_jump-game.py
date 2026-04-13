class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # [l, r] is the window of possible positions of every jump, every position in the window
        # needs to be considered to derive the next window
        l = r = 0

        while r < len(nums) - 1:
            # within this window, what's the farthest we can go
            farthest = 0

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            # if farthest is beyond the last position, the last position is guaranteed to be reachable
            if farthest >= len(nums) - 1:
                return True

            # we've jumped and define next window to evaluate
            l = r + 1
            r = farthest

            # Once the window is reversed, it means we can't go any further
            if l > r:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.canJump([2,3,1,1,4]) == True
    assert solution.canJump([3,2,1,0,4]) == False
    assert solution.canJump([2,0]) == True
    assert solution.canJump([2,0,0]) == True
    assert solution.canJump([2,5,0,0]) == True
