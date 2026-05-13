class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        import math

        m = len(potions)
        # sort the potions to prepare for binary search
        potions.sort()

        successful = []

        # for i in range(n):
        for spell in spells:
            # min potion so that spell * potion >= success
            min_potion = math.ceil(success / spell)
            # do a binary search, get the index of potion that is at least min_potion
            i = 0
            j = m - 1
            min_index = -1

            while j >= i:
                mid = (i + j) // 2
                if potions[mid] >= min_potion:
                    min_index = mid
                    j = mid - 1
                else:
                    i = mid + 1

            if min_index != -1:
                successful.append(m - min_index)
            else:
                successful.append(0)

        return successful


if __name__ == "__main__":
    solution = Solution()
    assert solution.successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7) == [4, 0, 3]
    assert solution.successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16) == [2, 0, 2]
