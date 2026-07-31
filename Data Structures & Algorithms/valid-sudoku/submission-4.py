class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        resCol = defaultdict(list)
        resRow = defaultdict(list)
        resSquare = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] in resCol[j]  or board[i][j] in resRow[i] or board[i][j] in resSquare[(i//3,j//3)]:
                    return False
                else:
                    if board[i][j] == ".":
                        continue
                    else:
                        resRow[i].append(board[i][j])
                        resCol[j].append(board[i][j])
                        resSquare[(i//3,j//3)].append(board[i][j])
        return True