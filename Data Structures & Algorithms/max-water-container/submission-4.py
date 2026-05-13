class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        first = 0
        last = len(heights) - 1
        while first < last:
            if heights[first] > heights[last]:
                max_area = max((last - first)*heights[last],max_area)
                last -= 1
            if heights[last] > heights[first]:
                max_area = max((last - first)*heights[first],max_area)
                first += 1
            if heights[last] == heights[first]:
                max_area = max((last - first)*heights[first],max_area)
                last -= 1
        return max_area

            
        