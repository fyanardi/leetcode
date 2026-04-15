class Solution:
    def removeStars(self, s: str) -> str:
        result = []

        for c in s:
            # result.pop() will cause error when result is empty, i.e. '*' at the start of the string
            # however it's guaranteed that "The operation above can be performed on s" so skip checking here
            if c == '*':
                result.pop()
            else:
                result.append(c)

        return ''.join(result)


if __name__ == "__main__":
    solution = Solution()
    assert solution.removeStars("leet**cod*e") == "lecoe"
    assert solution.removeStars("erase*****") == ""
