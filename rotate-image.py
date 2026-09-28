class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        for i in range(len(matrix) - 1):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# reverse vertically then transpose the matrix
# vertical reverse = flipping top to bottom
# transpose = flip over diagonal. matrix[i][j] = matrix[j][i]

# reverse then transpose the matrix
# input = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# solution = Solution()
# solution.rotate(input)
# for row in input:
#     print(row)
# # input = [
# #     [7,8,9],
# #     [4,5,6],
# #     [1,2,3]
# # ]
# # Output: [
# #     [7,4,1],
# #     [8,5,2],
# #     [9,6,3]
# # ]
