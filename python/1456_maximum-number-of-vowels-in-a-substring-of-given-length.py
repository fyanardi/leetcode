class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        l = len(s)

        max_vowels = 0
        num_vowels = 0

        # The num of vowels for the first k substring [0, k)
        for i in range(0, k):
            if s[i] in vowels:
                num_vowels += 1

        max_vowels = num_vowels

        for i in range(k, l):
            # The num of vowels for sliding window [i, i + k)
            if s[i - k] in vowels:
                num_vowels -= 1
            if s[i] in vowels:
                num_vowels += 1

            max_vowels = max(max_vowels, num_vowels)

        return max_vowels


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxVowels("abciiidef", 3) == 3
    assert solution.maxVowels("aeiou", 2) == 2
    assert solution.maxVowels("leetcode", 3) == 2
