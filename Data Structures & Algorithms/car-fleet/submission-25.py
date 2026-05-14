class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_number = 0
        res = []
        for i in range(len(position)):
            res.append([target-position[i],(target - position[i])/speed[i]])
        res.sort()
        res.reverse()
        while res:
            start_d,start_t = res.pop()
            if res == [] or res[-1][1] > start_t:
                fleet_number += 1
            else:
                while res and  res[-1][1] <= start_t:
                    res.pop()
                fleet_number += 1   
        return fleet_number


        




        