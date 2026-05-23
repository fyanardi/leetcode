function searchInsert(nums: number[], target: number): number {
    var left: number = 0;
    var right: number = nums.length - 1;
    var mid: number = -1;

    while (left <= right) {
        mid = Math.floor((right + left) / 2);
        if (nums[mid] == target) {
            return mid;
        }
        else if (nums[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return target > nums[mid] ? mid + 1 : mid;
};

console.assert(searchInsert([1, 3, 5, 6], 5) == 2, "Invalid output for input nums=[1, 3, 5, 6], target=5, expected=2")
console.assert(searchInsert([1, 3, 5, 6], 2) == 1, "Invalid output for input nums=[1, 3, 5, 6], target=2, expected=1")
console.assert(searchInsert([1, 3, 5, 6], 7) == 4, "Invalid output for input nums=[1, 3, 5, 6], target=7, expected=4")
console.assert(searchInsert([1, 3, 5, 6], 0) == 0, "Invalid output for input nums=[1, 3, 5, 6], target=0, expected=0")
