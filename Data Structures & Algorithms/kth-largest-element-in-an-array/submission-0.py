class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return []
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
        
        