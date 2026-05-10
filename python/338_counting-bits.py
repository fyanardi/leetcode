class Solution:
    def countBits(self, n: int) -> list[int]:
        if n == 0:
            return [0]

        # initialize for i = 0
        result = [0]

        i = 1
        pow = 0

        while i <= n:
            j = 0

            # 
            # 0 -> 0
            # ----------
            # 1 -> 1    -> 2^0
            # ----------
            # 2 -> 10   -> 2^1
            # 3 -> 11
            # ----------
            # 4 -> 100  -> 2^2
            # 5 -> 101
            # 6 -> 110
            # 7 -> 111
            # ----------
            # For every i in 2^x to 2^(x+1) - 1, the number of 1s is 1 more of the number of 1s at position i - 2^x
            # E.g. at position 5, the number of 1s is: 1 + number of 1s at position (5 - 2^2) = 1 + 1 = 2
            # Complexity: O(n)
            while j < (1 << pow) and i + j <= n:
                result.append(1 + result[j])
                j += 1

            pow += 1
            i += j

        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.countBits(2) == [0, 1, 1]
    assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]
