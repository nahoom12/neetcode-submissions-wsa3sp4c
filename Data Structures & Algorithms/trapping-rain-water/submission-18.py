class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        max_l = height[l]
        max_r = height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                max_l = max(height[l],max_l)
                res += max_l - height[l]
            else:
                r -= 1
                max_r = max(height[r],max_r)
                res += max_r - height[r]
        return res
        