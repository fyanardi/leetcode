import java.util.ArrayList;
import java.util.List;

/**
 * 1431. Kids With the Greatest Number of Candies
 */
public class Solution_1431 {
    static class Solution {
        public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
            int max_candies = 0;
            for (int c: candies) {
                if (c > max_candies) {
                    max_candies = c;
                }
            }
            List<Boolean> result = new ArrayList<>(candies.length);
            for (int c: candies) {
                if (c == max_candies) {
                    result.add(true);
                }
                else {
                    result.add(c + extraCandies >= max_candies);
                }
            }
            return result;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        assert solution.kidsWithCandies(new int[]{2, 3, 5, 1, 3}, 3).equals(List.of(true, true, true, false, true));
        assert solution.kidsWithCandies(new int[]{4, 2, 1, 1, 2}, 1).equals(List.of(true, false, false, false, false));
        assert solution.kidsWithCandies(new int[]{12, 1, 12}, 10).equals(List.of(true, false, true));
    }
}
