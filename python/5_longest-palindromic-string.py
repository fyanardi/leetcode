class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""

        for i in range(len(s)):
            p = self.palindrome(s, i, i)

            # check palindrome started with a single letter
            if len(p) > len(longest_palindrome):
                longest_palindrome = p

            # check palindrome started with 2 same letters
            if i + 1 < len(s) and s[i] == s[i + 1]:
                p = self.palindrome(s, i, i + 1)

                if len(p) > len(longest_palindrome):
                    longest_palindrome = p

        return longest_palindrome

    def palindrome(self, s: str, start: int, end: int) -> str:
        if start - 1 >= 0 and end + 1 < len(s):
            if s[start - 1] == s[end + 1]:
                return self.palindrome(s, start - 1, end + 1)

        return s[start:end+1]


if __name__ == "__main__":
    solution = Solution()

    print(solution.longestPalindrome("babad"))
    print(solution.longestPalindrome("cbbd"))
