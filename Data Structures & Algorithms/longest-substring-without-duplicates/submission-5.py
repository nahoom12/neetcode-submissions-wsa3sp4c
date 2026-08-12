class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        look_set = set()
        l = 0
        r =  0
        max_window = 0
        while r <= len(s) - 1:
            if s[r] not in look_set or look_set == ():
                look_set.add(s[r])
                current_window = r - l + 1
                r += 1
            else:
                while s[l] != s[r]:
                    look_set.remove(s[l])
                    l += 1
                look_set.remove(s[l])
                look_set.add(s[r])
                l += 1
                current_window =  r - l + 1
                r +=1
            max_window = max(current_window,max_window)
        return max_window
                
        




        