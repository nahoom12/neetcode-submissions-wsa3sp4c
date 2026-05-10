class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_hash = defaultdict(list)
        row_hash = defaultdict(list)
        square_hash = defaultdict(list)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in col_hash[c] or board[r][c] in row_hash[r] or board[r][c] in square_hash[r//3,c//3]:
                    return False
                else:
                    col_hash[c].append(board[r][c])
                    row_hash[r].append(board[r][c])
                    square_hash[r//3,c//3].append((board[r][c]))
        return True 
        