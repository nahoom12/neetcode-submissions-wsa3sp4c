class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        closed = 0
        opened = 0
        path = []
        res = []
        def backtracking(closed,opened):
            if closed == opened == n:
                res.append("".join(path))
            if opened < n:
                path.append("(")
                backtracking(closed,opened + 1)
                path.pop()
            if closed < opened:
                path.append(")")
                backtracking(closed + 1,opened)
                path.pop()
        backtracking(0,0)
        return res
            
        


