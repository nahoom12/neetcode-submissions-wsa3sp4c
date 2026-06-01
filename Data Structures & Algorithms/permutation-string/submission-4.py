class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countA = {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            countA[s1[i]] = 1 + countA.get(s1[i],0)
        countS = {}
        for i in range(len(s1)):
            countS[s2[i]] = 1 + countS.get(s2[i],0)
        if countS == countA:
            return True
        r = len(s1)
        l = 0
        while r <= len(s2) - 1:
            countS[s2[r]] = 1 + countS.get(s2[r],0)
            countS[s2[l]] = countS[s2[l]] - 1
            if countS[s2[l]] == 0:
                del countS[s2[l]]
            if countS == countA:
                return True
            r += 1
            l += 1
        return False


        


        

            
            

            


