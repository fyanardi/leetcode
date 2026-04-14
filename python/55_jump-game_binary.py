class Solution:
    # A solution that uses binary flags to keep track of whether each position can reach the last
    # position. This is not the ideal greedy algorithm, but the runtime for this algorithm is still
    # O(n) due to the use of bitwise operations to calculate & evaluate the bit flags
    def canJump(self, nums: list[int]) -> bool:
        # bit flags whether it is possible to reach the last index from each position
        # first position is at bit position n-1, last position is at bit position 0
        # initialize the last index (position 0) to be reachable
        reachability = 1
        n = len(nums)

        for i in range(n - 2, -1, -1):
            # nums[i] means current no jump is possible (last index is not reachable)
            if nums[i] == 0:
                continue
            # mask is all 1s in binary, e.g. if nums[i] = 2, mask = b'11 which is 2^2 - 1 = 3
            mask = (1 << min(nums[i], n - 1 - i)) - 1
            if n - 1 - i > nums[i]:
                # if the last reachable position for i is not the last index, shift the mask
                # to the left by n - i - nums[i]
                mask <<= n - 1 - i - nums[i]

            if reachability & mask:
                # turning on the reachability bit for i
                reachability |= 1 << (n - 1 - i)

        return (reachability >> n - 1) != 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.canJump([2, 3, 1, 1, 4]) == True
    assert solution.canJump([3, 2, 1, 0, 4]) == False
    assert solution.canJump([0, 2, 3]) == False
    assert solution.canJump([1, 2, 3]) == True
