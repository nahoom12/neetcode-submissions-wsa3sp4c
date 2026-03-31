class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        first = 0
        last = len(heights) - 1
        while first < last:
            if heights[first] <= heights[last]:
                max_a =  max(max_a,heights[first]*(last - first))
                first += 1
            elif heights[first] >= heights[last]:
                max_a = max(max_a,heights[last] *(last - first))
                last -= 1
        return max_a
            
            

        