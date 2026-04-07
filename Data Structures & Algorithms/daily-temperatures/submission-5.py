class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [ 0 for i in range(len(temperatures))]
        for i,num in enumerate(temperatures):
            while stack and stack[-1][1] < num:
                st_ind,st_num = stack.pop()
                res[st_ind] = i - st_ind
            stack.append([i,num])
        return res



    