class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths: list[list[int]] = [
            [0 for _ in range(n)]
            for _ in range(m)
        ]
        # at destination, there's only one unique path
        paths[m-1][n-1] = 1

        # iterate rows & columns, starting from the destination (m-1, n-1)
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r < m - 1:
                    paths[r][c] += paths[r+1][c]
                if c < n - 1:
                    paths[r][c] += paths[r][c+1]

        return paths[0][0]


if __name__ == "__main__":
    solution = Solution()

    assert solution.uniquePaths(m=3, n=7) == 28
    assert solution.uniquePaths(m=3, n=2) == 3
    assert solution.uniquePaths(m=23, n=12) == 193536720
