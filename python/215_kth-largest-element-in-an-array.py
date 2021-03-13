from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return None

        max_heap = MaxHeap()
        for n in nums:
            max_heap.insert(n)

        k_th_largest = None
        for i in range(k):
            k_th_largest = max_heap.pop()

        return k_th_largest


class MaxHeap:
    def __init__(self):
        self.harray = []


    def insert(self, n):
        debug = n == 520
        self.harray.append(n)
        i = len(self.harray) - 1
        i_p = self.__get_parent(i)
        while i != 0 and self.harray[i] > self.harray[i_p]:
            temp = self.harray[i]
            self.harray[i] = self.harray[i_p]
            self.harray[i_p] = temp
            i = i_p
            i_p = self.__get_parent(i)


    def pop(self):
        head = self.harray[0]
        self.harray[0] = self.harray[len(self.harray)-1]
        self.harray.pop(len(self.harray)-1)
        n = len(self.harray)
        i = 0
        left = self.__get_left(i)
        right = self.__get_right(i)
        while (left < n and self.harray[i] < self.harray[left]) or \
                (right < n and self.harray[i] < self.harray[right]):
            if right >= n or self.harray[right] < self.harray[left]:
                temp = self.harray[i]
                self.harray[i] = self.harray[left]
                self.harray[left] = temp
                i = left
            else:
                temp = self.harray[i]
                self.harray[i] = self.harray[right]
                self.harray[right] = temp
                i = right

            left = self.__get_left(i)
            right = self.__get_right(i)

        return head


    def __get_parent(self, i):
        return (i - 1) // 2


    def __get_left(self, i):
        return i * 2 + 1


    def __get_right(self, i):
        return i * 2 + 2


if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print(solution.findKthLargest(nums, k)) # 5

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(solution.findKthLargest(nums, k)) # 4

    nums = [-1, 2, 0]
    k = 1
    print(solution.findKthLargest(nums, k)) # 4

    # Random test cases
    import random
    solution = Solution()
    for i in range(10, 50):
        nums = []
        for j in range(i):
            nums.append(random.randint(-1000, 1000))

        sorted_nums = sorted(nums[:], reverse=True)
        print('nums:', nums)
        print('sorted_nums:', sorted_nums)

        for j in range(i):
            v = solution.findKthLargest(nums, j+1)
            print('k:', j+1, 'v:', v, 'expected:', sorted_nums[j])
            if v != sorted_nums[j]:
                print('#### FAILED #####')
                exit()

