class Solution:
    def myAtoi(self, s: str) -> int:
        result: int | None = None
        sign: int | None = None

        for i in range(len(s)):
            if result is None:
                # skip leading whitespaces
                if s[i] == ' ':
                    continue
                # no digits & sign encountered
                elif sign is None:
                    # '-' -> negative
                    if s[i] == '-':
                        sign = -1
                        # immediately assign result to avoid allowing whitespaces after '-' sign
                        result = 0
                    # '+' -> positive
                    elif s[i] == '+':
                        sign = 1
                        result = 0
                    elif s[i] >= '0' and s[i] <= '9':
                        sign = 1
                        result = ord(s[i]) - ord('0')
                    else:
                        # invalid character before any sign or digits, discard the rest
                        break
                elif sign is not None:
                    if s[i] >= '0' and s[i] <= '9':
                        result = ord(s[i]) - ord('0')
                    else:
                        # invalid character
                        break
            else:
                if s[i] >= '0' and s[i] <= '9':
                    result = result * 10 + ord(s[i]) - ord('0')
                else:
                    # invalid character
                    break

        if result is not None:
            max_signed_int = 1 << 31
            # sign is always not None if result is not None
            if sign == 1 and result >= max_signed_int:
                return max_signed_int - 1
            elif sign == -1 and result > max_signed_int:
                return -1 * max_signed_int

        return (
            sign * result
            if sign is not None and result is not None
            else (
                result if result is not None else 0
            )
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.myAtoi("42") == 42
    assert solution.myAtoi(" -42") == -42
    assert solution.myAtoi("1337c0d3") == 1337
    assert solution.myAtoi("0-1") == 0
    assert solution.myAtoi("words and 987") == 0
    assert solution.myAtoi("2147483647") == 2147483647 # 2^31 - 1
    assert solution.myAtoi("2147483648") == 2147483647 # 2^31 (rounded down to 2^31 - 1)
    assert solution.myAtoi("-2147483648") == -2147483648 # -2^31
    assert solution.myAtoi("-2147483649") == -2147483648  # -2^31 - 1 (rounded up to -2^31)
    assert solution.myAtoi("  +  413") == 0
