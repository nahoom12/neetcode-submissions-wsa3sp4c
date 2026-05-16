class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            first = 0
            last = m - 1
            while first <= last:
                mid = (first + last)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    first = mid + 1
                else:
                    last = mid - 1
        return False



            
             

            
            


                


        