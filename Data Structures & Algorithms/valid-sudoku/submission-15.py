class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowseen=[]
        colseen=[]
        for _ in range(9):
            rowseen.append(set())
            colseen.append(set())
        
        grid = set()
        r=0
        while r < len(board)-2:
            #traverses each grid
            
            c=0
            while c<len(board[0])-2:
                i=r
                
                finish = i
                while i< finish+3:
                    
                    j=c
                    f = j
                    while j<f+3:
                        
                        print(i,j)
                        if board[i][j]!=".":
                            if board[i][j] in grid:
                                
                                return False
                            else:
                                grid.add(board[i][j])
                            if board[i][j] in rowseen[i]:
                                print("row")
                                return False
                            else:
                                rowseen[i].add(board[i][j])
                            if board[i][j] in colseen[j]:
                                print("col")
                                
                                return False
                            else:
                                colseen[j].add(board[i][j])
                    
                        j+=1
                    i+=1
                grid.clear()
                                
                        
                
                
                c+=3
                
                

            r+=3
        return True