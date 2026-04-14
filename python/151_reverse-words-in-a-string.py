class Solution:
    def reverseWords(self, s: str) -> str:
        reversed = []
        # split with sep argument will split based on whitespaces and trim any leading/trailing whitespaces
        words = s.split()

        for i in range(len(words) - 1, -1, -1):
            reversed.append(words[i])

        return ' '.join(reversed)


if __name__ == "__main__":
    solution = Solution()
    assert solution.reverseWords("the sky is blue") == "blue is sky the"
    assert solution.reverseWords("  hello world  ") == "world hello"
    assert solution.reverseWords("a good   example") == "example good a"
