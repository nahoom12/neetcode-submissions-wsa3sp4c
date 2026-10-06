import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points)  == k:
            return points
        if k > len(points):
            return []
        res = []
        ret = []
        store = defaultdict(list)
        for i in range(len(points)):
            a,b = points[i]
            distance = math.sqrt(a**2 + b**2)
            store[distance].append(points[i])
            res.append(distance)
        heapq.heapify(res)
        while len(ret) < k:
            x = heapq.heappop(res)
            if x not in store:
                continue
            for num in store[x]:
                ret.append(num)
                if len(ret) == k:
                    return ret
            del store[x]
            


        


        
        