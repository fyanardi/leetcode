class Solution:
    def decodeString(self, s: str) -> str:
        # Any assertion indicates error in the encoded string syntax

        # final decoded string
        decoded = ""

        # variables to keep track of count & letters to be decoded, they will be None when we're
        # not in an encoded string
        count = None
        letters = None

        # stack to keep track of nested encoded strings
        stack = []

        for c in s:
            if c >= '0' and c <= '9':
                # there is an existing encoded string, push it to the stack and switch to the new
                # nested encoded string
                if letters is not None:
                    stack.append((count, letters))
                    count = None
                    letters = None

                if count is None:
                    count = int(c)
                else:
                    count = count * 10 + int(c)
            elif c == '[':
                # inside encoded string
                letters = ''
            elif c == ']':
                # end of encoded string, decode it
                assert count is not None
                assert letters is not None

                if len(stack) == 0:
                    decoded += letters * count
                    count = None
                    letters = None
                else:
                    repeated = letters * count
                    # restore the stack and update the current decoded
                    count, letters = stack.pop()
                    letters += repeated
            elif c >= 'a' and c <= 'z':
                if count is None:
                    # we're not in an encoded string, just append directly to the decoded string
                    decoded += c
                else:
                    assert letters is not None
                    letters += c

        return decoded


if __name__ == "__main__":
    solution = Solution()

    assert solution.decodeString("3[a]2[bc]") == "aaabcbc"
    assert solution.decodeString("3[a2[c]]") == "accaccacc"
    assert solution.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert solution.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
    assert solution.decodeString("3[a10[bc]]") == "abcbcbcbcbcbcbcbcbcbcabcbcbcbcbcbcbcbcbcbcabcbcbcbcbcbcbcbcbcbc"
