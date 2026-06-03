class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        lengths: list[list[int]] = [
            [0 for _ in range(m+1)]
            for _ in range(n+1)
        ]

        for i in range(1, n+1, 1):
            for j in range(1, m+1, 1):
                if text1[i-1] == text2[j-1]:
                    lengths[i][j] = 1 + lengths[i-1][j-1]
                else:
                    lengths[i][j] = max(lengths[i-1][j], lengths[i][j-1])

        return lengths[n][m]


if __name__ == "__main__":
    solution = Solution()

    assert solution.longestCommonSubsequence(text1="abcde", text2="ace") == 3
    assert solution.longestCommonSubsequence(text1="abc", text2="abc") == 3
    assert solution.longestCommonSubsequence(text1="abc", text2="def") == 0
    assert solution.longestCommonSubsequence(text1="pmjghexybyrgzczy", text2="hafcdqbgncrcbihkd") == 0
