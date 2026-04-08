class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftList = 0
        rightList = len(matrix) - 1
        

        while leftList <= rightList:
            midList = (leftList + rightList) // 2
            currList = matrix[midList]
            
            leftNum = currList[0]
            rightNum = currList[-1]

            if leftNum <= target <= rightNum:
                if target in currList:
                    return True
                return False
                
            else:
                if leftNum > target:
                    rightList = midList - 1
                else:
                    leftList = midList + 1
        return False
