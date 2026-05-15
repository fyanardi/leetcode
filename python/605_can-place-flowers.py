class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        l = len(flowerbed)
        new_flowerbed = [f for f in flowerbed]
        plantable = 0
        i = 0

        while i < l:
            if new_flowerbed[i] == 1:
                # this position has a flower planted, skip the next one
                i += 2
                continue
            if i == 0:
                if i + 1 > l - 1 or new_flowerbed[i+1] == 0:
                    new_flowerbed[i] = 1
                    plantable += 1
            elif i == l - 1:
                if i - 1 >= 0 and new_flowerbed[i-1] == 0:
                    new_flowerbed[i] = 1
                    plantable += 1
            elif new_flowerbed[i-1] == 0 and new_flowerbed[i+1] == 0:
                new_flowerbed[i] = 1
                # mark this position plantable, skip the next one
                i += 1
                plantable += 1

            i += 1
            if plantable >= n:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1) == True
    assert solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2) == False
    assert solution.canPlaceFlowers(flowerbed=[0, 0, 1, 0, 1], n=1) ==  True
    assert solution.canPlaceFlowers(flowerbed=[1, 0, 1, 0, 1, 0, 1], n=0) == True
    assert solution.canPlaceFlowers(flowerbed=[0, 1, 0], n=1) == False
    assert solution.canPlaceFlowers(flowerbed=[0], n=1) == True
