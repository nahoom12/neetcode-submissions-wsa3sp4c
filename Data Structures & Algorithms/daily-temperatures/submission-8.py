class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [ 0 for i in range(len(temperatures))]
        stack = []
        for i,num in enumerate(temperatures):
            while stack and stack [-1][1] < num:
                index,number = stack.pop()
                res[index] =  i - index
            stack.append([i,num])
        return res


      




        



        