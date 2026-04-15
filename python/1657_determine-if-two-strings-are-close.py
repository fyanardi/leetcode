class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        # both dicts contain the frequency of each letter in word1 and word2, respectively
        chars1: dict[str, int] = {}
        chars2: dict[str, int] = {}

        # count the frequency of each letters in word1 and word2
        for c in word1:
            if c not in chars1:
                chars1[c] = 1
            else:
                chars1[c] += 1

        for c in word2:
            if c not in chars2:
                chars2[c] = 1
            else:
                chars2[c] += 1

        return (
            # 1: both words have the same set of letters
            set(chars1.keys()) == set(chars2.keys())
            # 2: the frequencies of letters are exactly the same (regardless of the corresponding letters)
            and sorted(chars1.values()) == sorted(chars2.values())
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.closeStrings("abc", "bca") == True
    assert solution.closeStrings("a", "aa") == False
    assert solution.closeStrings("cabbba", "abbccc") == True
    assert solution.closeStrings("uau", "ssx") == False
