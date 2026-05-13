class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_set = {')':'(','}':'{',']':'['}
        if len(s) == 1:
            return False
        for i in range(len(s)):
            if not stack or s[i] in hash_set.values():
                stack.append(s[i])
            elif s[i] in hash_set and hash_set[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False 
        if stack == []:
            return  True
        else:
            return False
        