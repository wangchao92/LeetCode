class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            pos = [i, 0]
            for j in range(min(m - i, n)):
                if j == 0:
                    num = matrix[pos[0]][pos[1]]
                else:
                    if matrix[pos[0]][pos[1]] != num:
                        return False
                pos[0] += 1
                pos[1] += 1
        for j in range(1, n):
            pos = [0, j]
            for i in range(min(n - j, m)):
                if i == 0:
                    num = matrix[pos[0]][pos[1]]
                else:
                    if matrix[pos[0]][pos[1]] != num:
                        return False
                pos[0] += 1
                pos[1] += 1
        return True
