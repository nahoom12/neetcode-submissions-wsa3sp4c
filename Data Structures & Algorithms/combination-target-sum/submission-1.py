class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total = 0
        res = []
        def backtracking(start_index,path,total):
            if total == target:
                res.append(path.copy())
                return
            if total > target or start_index >= len(nums):
                return
            for i in range(start_index,len(nums)):
                path.append(nums[i])
                backtracking(i,path,total + nums[i])
                path.pop()
        backtracking(0,[],0)
        return res
    
        