from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            top = matrix[i][i:n-i]

            right = []
            for j in range(i, n-i):
                right.append(matrix[j][n-i-1])

            bottom = []            
            for j in range(i, n-i):
                bottom.append(matrix[n-i-1][j])

            left = []
            for j in range(i, n-i):
                left.append(matrix[j][i])

            # print('i:', i, 'top:', top, 'right:', right, 'bottom:', bottom, 'left:', left)

            # top -> right
            for j in range(i, n-i):
                matrix[j][n-i-1] = top[j-i]
            # right -> bottom
            for j in range(i, n-i):
                matrix[n-i-1][j] = right[n-i-j-1]
            # bottom -> left
            for j in range(i, n-i):
                matrix[j][i] = bottom[j-i]
            # left -> top
            for j in range(i, n-i):
                matrix[i][j] = left[n-i-j-1] 


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution.rotate(matrix)
    # Expected output: [[7,4,1],[8,5,2],[9,6,3]]
    print(matrix)

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate(matrix)
    # Expected output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print(matrix)

    matrix = [[1]]
    solution.rotate(matrix)
    # Expected output: [[1]]
    print(matrix)

    matrix = [[1,2],[3,4]]
    solution.rotate(matrix)
    # Expected output: [[3,1],[4,2]]
    print(matrix)

