class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        substring = ''
        start_substring = 0
        last_index_map = {}
        for i in range(len(s)):
            if s[i] in substring:
                substring = substring[last_index_map[s[i]] - start_substring + 1:] + s[i]
                start_substring = last_index_map[s[i]] + 1
                last_index_map[s[i]] = i
            else:
                substring = substring + s[i]
            last_index_map[s[i]] = i
            if len(substring) > max_len:
                max_len = len(substring)

        return max_len


if __name__ == "__main__":
    solution = Solution()

    print(solution.lengthOfLongestSubstring('abcabcbb')) # 3
    print(solution.lengthOfLongestSubstring('bbbbb')) # 1
    print(solution.lengthOfLongestSubstring('pwwkew')) #3
    print(solution.lengthOfLongestSubstring('')) # 0
    print(solution.lengthOfLongestSubstring('bbtablud')) #6

