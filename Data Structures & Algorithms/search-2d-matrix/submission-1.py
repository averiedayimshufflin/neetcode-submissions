class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1
        
        while top <= bottom:
            
            left=0
            right=len(matrix[0])-1
            

            row_mid=top+(bottom-top//2)
            
            if target>= matrix[row_mid][0] and target<=matrix[row_mid][-1]:
                
                while left<=right:
                    mid = left+(right-left//2)
                    if target==matrix[row_mid][mid]:
                        return True
                    elif target>matrix[row_mid][mid]:
                        left=mid+1
                    else:
                        right=mid-1
                return False
                    
            elif target>matrix[row_mid][0]:
                top=row_mid+1
            else:
                
                bottom=row_mid-1

        

        return False    
            
        


        