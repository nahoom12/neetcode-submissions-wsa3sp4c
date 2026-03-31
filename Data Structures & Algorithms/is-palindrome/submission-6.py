class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = s.lower()
        #clean.replace(" ","")
        clean = "".join( char for char in clean if char.isalnum())
        first = 0
        last = len(clean) - 1
        while first <= last:
            if clean[first] == clean[last]:
                first = first + 1
                last = last -1
            else:
                return False
        return True
