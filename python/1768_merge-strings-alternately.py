class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        merged = ""

        for i in range(0, min(l1, l2)):
            merged += word1[i] + word2[i]

        if l1 > l2:
            merged += word1[l2:]
        else:
            merged += word2[l1:]

        return merged


if __name__ == "__main__":
    solution = Solution()
    assert solution.mergeAlternately("abc", "pqr") == "apbqcr"
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert solution.mergeAlternately("abcd", "pq") == "apbqcd"
    assert solution.mergeAlternately("", "pqrs") == "pqrs"
    assert solution.mergeAlternately("abcd", "") == "abcd"
