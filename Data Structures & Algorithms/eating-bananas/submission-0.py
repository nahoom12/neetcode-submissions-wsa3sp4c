import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,max(piles)
        res = right
        while left <= right:
            mid = (left + right)//2
            rate_sum = 0
            for i in range(len(piles)):
                rate_sum  += math.ceil(piles[i] / mid)
            if rate_sum <= h:
                res = min(res,mid)
                right = mid - 1
            else:
                left = mid + 1     
        return res
            

        

        
        