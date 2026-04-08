from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        cols = len(matrix[0])
        rows = len(matrix)
        l, r = 0, (cols * rows) - 1

        while l <= r:
            mid = l + (r - l) // 2

            col = mid % cols
            row = mid // cols
            midVal = matrix[row][col]
            
            if midVal < target:
                l = mid + 1
            elif midVal > target:
                r = mid - 1
            else:
                return True
        return False    




