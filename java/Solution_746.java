import java.util.Arrays;

/**
 * 746. Min Cost Climbing Stairs
 */
public class Solution_746 {
    static class Solution {
        public int minCostClimbingStairs(int[] cost) {
            int n = cost.length;
            if (n == 1) {
                return cost[0];
            }
            else if (n == 2) {
                return Math.min(cost[0], cost[1]);
            }

            int[] minCost = new int[n];
            minCost[n-1] = cost[n-1];
            minCost[n-2] = cost[n-2];

            for (int i = n-3; i >= 0; i--) {
                minCost[i] = cost[i] + Math.min(minCost[i+1], minCost[i+2]);
            }

            return Math.min(minCost[0], minCost[1]);
        }
    }

    // Run with -ea to enable assertions
    public static void main(String[] args) {
        Solution solution = new Solution();

        assert solution.minCostClimbingStairs(new int[]{10, 15, 20 }) == 15;
        assert solution.minCostClimbingStairs(new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}) == 6;
    }
}
