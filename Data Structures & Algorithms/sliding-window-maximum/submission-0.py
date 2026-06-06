class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        res1 = []
        for i in range(k):
            res.append(nums[i])
        res1.append(max(res))
        j = k
        l = 0
        while j <= len(nums) - 1:
            res.remove(nums[l])
            res.append(nums[j])
            res1.append(max(res))
            j += 1
            l += 1
        return res1



        
        
        
        




        