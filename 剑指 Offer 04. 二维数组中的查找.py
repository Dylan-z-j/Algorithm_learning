class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix in [[], [[]]]:
            return False

        # 从右上角看是二叉树搜索        
        n = 0
        m = len(matrix[0]) - 1
        curr_node = matrix[n][m]

        while n < len(matrix) and m >= 0:

            # print(curr_node)

            curr_node = matrix[n][m]

            if curr_node == target:
                return True 
            elif curr_node > target:
                m -= 1
            elif curr_node < target:
                n += 1

        return False
                
