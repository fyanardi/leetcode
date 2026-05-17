class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)

        i = 0
        j = n - 1
        reversed = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while i < j:
            if reversed[i] in vowels:
                if reversed[j] in vowels:
                    reversed[i] = s[j]
                    reversed[j] = s[i]
                    i += 1
                # when s[j] is vowel, it has been swapped with s[i]
                # when s[j] is consonant, we need to advance j to find the next vowel
                j -= 1
            else:
                if reversed[j] not in vowels:
                    j -= 1
                i += 1

        return ''.join(reversed)


if __name__ == "__main__":
    solution = Solution()
    assert solution.reverseVowels("IceCreAm") == "AceCreIm"
    assert solution.reverseVowels("leetcode") == "leotcede"
