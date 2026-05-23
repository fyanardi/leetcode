/**
 * 1493. Longest Subarray of 1's After Deleting One Element
 */
public class Solution_1493 {
    static class Solution {
        public int longestSubarray(int[] nums) {
            int left = 0;
            int right = 0;
            int maxCount = 0;
            int deleted = -1;

            while (right < nums.length) {
                if (nums[right] == 1) {
                    right++;
                }
                else {
                    // If no '0' deleted yet, mark this '0' as deleted
                    if (deleted == -1) {
                        deleted = right;
                        right++;
                    }
                    else {
                        // right - left will exclude the deleted '0', -1 will exclude the current '0'
                        maxCount = Math.max(maxCount, right - left - 1);
                        left = right = deleted + 1;
                        deleted = -1;
                    }
                }
            }
            // handle case when there's no '0' in the array
            // right - left since right has been incremented by 1 earlier (now right == nums.length)
            // -1 will remove one of the '1'
            maxCount = Math.max(maxCount, right - left - 1);
            return maxCount;
        }
    }

    // Run with -ea to enable assertions
    public static void main(String[] args) {
        Solution solution = new Solution();

        assert solution.longestSubarray(new int[]{1, 1, 0, 1}) == 3;
        assert solution.longestSubarray(new int[]{0, 1, 1, 1, 0, 1, 1, 0, 1}) == 5;
        assert solution.longestSubarray(new int[]{1, 1, 1}) == 2;
    }
}
