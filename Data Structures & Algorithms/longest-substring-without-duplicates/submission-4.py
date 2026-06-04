class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        countS = set()
        l,r = 0,0
        count = 0
        while r <= len(s) - 1:
            if countS == () or s[r] not in countS:
                countS.add(s[r])
                count = max(count, r - l + 1)
            else:
                while s[l] != s[r]:
                    countS.remove(s[l])
                    l += 1 
                countS.remove(s[l])
                countS.add(s[r])
                l += 1
            r += 1
        return count
 
 
        