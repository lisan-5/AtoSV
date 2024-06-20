class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = [0, 3, 6, 9]
        b = [0, 3, 6, 9]
        
        
        for count in range(3):
            for count2 in range(3):
                arr = [-1] * 10
                for i in range(a[count], a[count+1]):
                    for j in range(b[count2], b[count2+1]):
                        if board[i][j] == ".":
                            continue
                        else:
                            if arr[int(board[i][j])] != -1:
                                
                                return False
                            else:
                                arr[int(board[i][j])] = 1
        
            
        for i in range(9):
            k = {}
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in k:
                    return False
                else:
                    k[board[i][j]] = 1
        for j in range(9):
            k = {}
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in k:
                    return False
                else:
                    k[board[i][j]] = 1
        return True
                    
            
            
