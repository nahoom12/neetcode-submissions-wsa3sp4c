class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        bool_val = [False]*len(nums)
        def backtracking(bool_val):
            if len(path) == len(nums):
                res.append(path.copy())
            for i in range(len(nums)):
                if bool_val[i]  == False:
                    path.append(nums[i])
                    bool_val[i] = True
                    backtracking(bool_val)
                    path.pop()
                    bool_val[i] = False
        backtracking(bool_val)
        return res
       
            

        