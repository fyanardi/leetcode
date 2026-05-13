class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) == 1:
            return list(map[digits[0]])

        result = []
        # recursive call to build the subsequent combinations
        subs = self.letterCombinations(digits[1:])
        for l in map[digits[0]]:
            for s in subs:
                result.append(l + s)

        return result


if __name__ == "__main__":
    solution = Solution()
    assert set(solution.letterCombinations("23")) == set(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    assert set(solution.letterCombinations("2")) == set(["a", "b", "c"])
