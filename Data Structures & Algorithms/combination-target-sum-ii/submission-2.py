class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(path,start_index,total):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return
            for i in range(start_index,len(candidates)):
                if i > start_index and candidates[i - 1] == candidates[i]:
                    continue
                path.append(candidates[i])
                dfs(path,i + 1,candidates[i] + total)
                path.pop()
        dfs([],0,0)
        return res

        