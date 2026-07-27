class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtracking():
            if len(path) == len(nums):
                res.append(path.copy())
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtracking()
                    path.pop()
        backtracking()
        return res
       
            

        