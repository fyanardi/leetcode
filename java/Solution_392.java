/**
 * 392. Is Subsequence
 */
public class Solution_392 {
    static class Solution {
        public boolean isSubsequence(String s, String t) {
            int i = 0;
            int j = 0;

            while (i < s.length() && j < t.length()) {
                if (s.charAt(i) == t.charAt(j)) {
                    if (i == s.length() - 1) {
                        return true;
                    }
                    i++;
                    j++;
                }
                else {
                    j++;
                }
            }

            return false;
        }
    }

    // Run with -ea to enable assertions
    public static void main(String[] args) {
        Solution solution = new Solution();

        assert solution.isSubsequence("abc", "ahbgdc") == true;
        assert solution.isSubsequence("axc", "ahbgdc") == false;
        assert solution.isSubsequence("", "ahbgdc") == true;
    }
}
