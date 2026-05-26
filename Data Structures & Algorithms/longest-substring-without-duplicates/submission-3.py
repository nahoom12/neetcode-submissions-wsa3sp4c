class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check_up = set()
        l = 0 
        res = 0
        for r in range(len(s)):
            while s[r] in check_up:
                check_up.remove(s[l])
                l += 1
            check_up.add(s[r])
            res = max(res,r - l + 1)
        return res



     
        