class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen = {")":"(","]":"[","}":"{"}
        if s[0] in closetoOpen:
            return False
        for c in s:
            if c in closetoOpen:
                if stack and stack[-1] == closetoOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False
                

            
            
            