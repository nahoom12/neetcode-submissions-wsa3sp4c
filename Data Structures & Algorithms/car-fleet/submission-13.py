class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0
        res = [ [] for i in range(len(position))]
        for i in range(len(position)):
            res[i] +=[target - position[i],(target - position[i])/speed[i]]
        res.sort()
        res.reverse()
        while res:
            short_d,t = res.pop()
            if  res == [] or t < res[-1][1]:
                count += 1
            else:
                while res and res[-1][1] <= t:
                    res.pop()
                count += 1
        return count
            





        
        



            



        