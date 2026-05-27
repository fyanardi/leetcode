import java.util.Arrays;

/**
 * 790. Domino and Tromino Tiling
 */
public class Solution_790 {
    static class Solution {
        final long MOD = 1000000007;

        public int numTilings(int n) {
            if (n == 1) {
                return 1;
            }
            if (n == 2) {
                return 2;
            }
            if (n == 3) {
                return 5;
            }
            long[] tiles = new long[n+1];
            tiles[0] = 1;
            tiles[1] = 1;
            tiles[2] = 2;
            tiles[3] = 5;

            for (int i = 4; i <= n; i++) {
                tiles[i] = (2L * tiles[i-1] + tiles[i-3]) % MOD;
            }

            return (int) tiles[n];
        }
    }

    // Run with -ea to enable assertions
    public static void main(String[] args) {
        Solution solution = new Solution();

        assert solution.numTilings(3) == 5;
        assert solution.numTilings(1) == 1;
        assert solution.numTilings(4) == 11;
        assert solution.numTilings(5) == 24;
    }
}
