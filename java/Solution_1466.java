import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

/**
 * 1466. Reorder Routes to Make All Paths Lead to the City Zero
 */
public class Solution_1466 {
    static class Solution {
        public int minReorder(int n, int[][] connections) {
            // Map of start -> end
            Map<Integer, List<Integer>> roads_by_start = new HashMap<>();
            // Map of end -> start
            Map<Integer, List<Integer>> roads_by_end = new HashMap<>();
            Stack<Integer> stack = new Stack<>();
            int reorder = 0;

            Boolean[] visited = new Boolean[n];
            Arrays.fill(visited, false);

            for (int[] connection: connections) {
                int start = connection[0];
                int end = connection[1];
                if (!roads_by_start.containsKey(start)) {
                    roads_by_start.put(start, new ArrayList<>());
                }
                if (!roads_by_end.containsKey(end)) {
                    roads_by_end.put(end, new ArrayList<>());
                }
                roads_by_start.get(start).add(end);
                roads_by_end.get(end).add(start);
            }

            stack.push(0);

            while (!stack.isEmpty()) {
                int start = stack.pop();
                visited[start] = true;
                if (roads_by_start.containsKey(start)) {
                    for (int end: roads_by_start.get(start)) {
                        if (!visited[end]) {
                            stack.push(end);
                            reorder++;
                        }
                    }
                }
                if (roads_by_end.containsKey(start)) {
                    for (int end: roads_by_end.get(start)) {
                        if (!visited[end]) {
                            stack.push(end);
                        }
                    }
                }
            }

            return reorder;
        }
    }

    // Run with -ea to enable assertions
    public static void main(String[] args) {
        Solution solution = new Solution();

        assert solution.minReorder(6, new int[][]{{0, 1}, {1, 3}, {2, 3}, {4, 0}, {4, 5}}) == 3;
        assert solution.minReorder(5, new int[][]{{1, 0}, {1, 2}, {3, 2}, {3, 4}}) == 2;
        assert solution.minReorder(3, new int[][]{{1, 0}, {2, 0}}) == 0;
        assert solution.minReorder(6, new int[][]{{4, 5}, {0, 1}, {1, 3}, {2, 3}, {4, 0}}) == 3;
    }
}
