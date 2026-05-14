class Solution:
    def tribonacci(self, n: int) -> int:
        trib: list[int] = [0, 1, 1]

        if n < 3:
            return trib[n]

        for i in range(3, n + 1):
            trib.append(0)
            for j in range(1, 4):
                trib[i] += trib[i - j]

        return trib[n]


if __name__ == "__main__":
    solution = Solution()
    assert solution.tribonacci(4) == 4
    assert solution.tribonacci(25) == 1389537
