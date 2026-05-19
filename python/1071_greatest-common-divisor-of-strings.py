class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def factorize(n: int) -> list[int]:
            import math
            if n == 1:
                return [1]

            s = int(math.sqrt(n))
            factors = [1, n]
            for i in range(2, s+1):
                if n % i == 0:
                    factors.append(i)
                    factors.append(int(n / i))

            return sorted(set(factors), reverse=True)

        def divides(s, t) -> bool:
            return s == t * (int(len(s) / len(t)))

        l1 = len(str1)
        l2 = len(str2)

        f1 = factorize(l1)
        f2 = factorize(l2)

        if l2 < l1:
            for f in f2:
                if f not in f1:
                    continue
                if divides(str1, str2[0:f]) and divides(str2, str2[0:f]):
                    return str2[0:f]
        else:
            for f in f1:
                if f not in f2:
                    continue
                if divides(str2, str1[0:f]) and divides(str1, str1[0:f]):
                    return str1[0:f]

        return ""


if __name__ == "__main__":
    solution = Solution()

    assert solution.gcdOfStrings(str1="ABCABC", str2="ABC") == "ABC"
    assert solution.gcdOfStrings(str1="ABABAB", str2="ABAB") == "AB"
    assert solution.gcdOfStrings(str1="LEET", str2="CODE") == ""
    assert solution.gcdOfStrings(str1="AAAAAB", str2="AAA") == ""
