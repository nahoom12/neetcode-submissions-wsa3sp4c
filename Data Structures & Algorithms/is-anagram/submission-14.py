class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        storage ={}
        for i in range(len(s)):
            if s[i] in storage:
                storage[s[i]]+=1
            else:
                storage[s[i]]= 1  
        for i in range (len(t)):
            if t[i] in storage:
                storage[t[i]] -= 1
                if storage[t[i]] < 0:
                    return False
            else:
                return False     
        return True



