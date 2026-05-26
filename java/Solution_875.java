import java.util.Arrays;

/**
 *
 */
public class Solution_875 {
    static class Solution {
        private boolean finishEating(int[] piles, int h, int k) {
            int hours = 0;
            for (int p: piles) {
                hours += Math.ceil(1.0 * p/k);
            }
            return hours <= h;
        }

        private int maxPiles(int[] piles) {
            int max = 0;
            for (int p: piles) {
                max = Math.max(max, p);
            }
            return max;
        }

        public int minEatingSpeed(int[] piles, int h) {
            int left = 1;
            int right = maxPiles(piles);

            while (left <= right) {
                int mid = (int) Math.floor((left + right) / 2);
                if (finishEating(piles, h, mid)) {
                    right = mid - 1;
                }
                else {
                    left = mid + 1;
                }
            }

            return left;
        }
    }

    // Run with -ea to enable assertions
    public static void main(String[] args) {
        Solution solution = new Solution();

        assert solution.minEatingSpeed(new int[]{3, 6, 7, 11}, 8) == 4;
        assert solution.minEatingSpeed(new int[]{30, 11, 23, 4, 20}, 5) == 30;
        assert solution.minEatingSpeed(new int[]{30, 11, 23, 4, 20}, 6) == 23;
        assert solution.minEatingSpeed(new int[]{312884470}, 312884469) == 2;
        assert solution.minEatingSpeed(new int[]{
            332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316,
            877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184
        }, 823855818) == 14;
    }
}
