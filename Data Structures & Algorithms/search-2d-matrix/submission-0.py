class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        left, right = 0, ROWS * COLS

        while left < right:
            # Get 1D mid coordinate
            mid = left + (right - left) // 2

            # convert mid to 2D coordinates
            row = mid // COLS
            col = mid % COLS

            if target > matrix[row][col]:
                left = mid + 1
            elif target < matrix[row][col]:
                right = mid
            else:
                return True
        
        return False
