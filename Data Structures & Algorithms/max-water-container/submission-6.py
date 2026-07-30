class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        Area = 0
        while l <= r:
            if heights[l] <= heights[r]:
                Area = max(heights[l]*(r-l),Area)
                l += 1
            else:
                Area = max(heights[r]*(r-l),Area)
                r -= 1
        return Area



            


        