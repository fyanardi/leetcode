class Solution:
    def jump(self, nums: list[int]) -> int:
        l = len(nums)
        max_int = 1 << 31 - 1
        # min jumps at every position, initialized with max int except the last position which is
        # the destination
        min_jumps = [max_int for _ in range(l)]
        min_jumps[l - 1] = 0

        for i in range(l - 2, -1, -1):
            # at every position i, minimize the number of jumps by checking against jumping by j
            # (1 <= j <= nums[i])
            # to position i + j
            for j in range(1, nums[i] + 1):
                if i + j >= l:
                    break
                min_jumps[i] = min(1 + min_jumps[i + j], min_jumps[i])

        return min_jumps[0]


if __name__ == "__main__":
    solution = Solution()
    assert solution.jump([2,3,1,1,4]) == 2
    assert solution.jump([2,3,0,1,4]) == 2
    assert solution.jump([1,3,5,8,9,2,6,7,6,8,9]) == 3
    assert solution.jump([1,4,3,2,6,7]) == 2
