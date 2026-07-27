class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        def dfs(path,start_index):
            res.append(path.copy())
            for i in range(start_index,len(nums)):
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(path,i + 1)
                path.pop()
        dfs([],0)
        return res

        


        