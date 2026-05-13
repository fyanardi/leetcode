class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        def combination_sum(path: list[int], nums: list[int], k: int, n: int, combinations):
            if k == 1:
                if n <= 9 and n in nums:
                    combinations.append(path + [n])
                return

            for i in range(len(nums)):
                num = nums[i]
                # if num is bigger than or equal n, we can't use this num
                if num >= n:
                    continue
                combination_sum(path + [num], nums[i+1:], k - 1, n - num, combinations)

        combinations = []
        combination_sum([], list(range(1, 10)), k, n, combinations)
        return combinations


def assert_combinations_equal(actual: list[list[int]], expected: list[list[int]]):
    assert len(actual) == len(expected)

    actual_set = [set(c) for c in actual]

    for e in expected:
        assert set(e) in actual_set, f"{e} is not found in actual"


if __name__ == "__main__":
    solution = Solution()
    assert_combinations_equal(
        actual=solution.combinationSum3(k=3, n=7),
        expected=[[1, 2, 4]],
    )
    assert_combinations_equal(
        actual=solution.combinationSum3(k=3, n=9),
        expected=[[1, 2, 6], [1, 3, 5], [2, 3, 4]],
    )
    assert_combinations_equal(
        actual=solution.combinationSum3(k=4, n=1),
        expected=[],
    )
