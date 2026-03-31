class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visited = []
        res = defaultdict(int)
        for num in nums:
            if num in visited:
                res[num] += 1
            else:
                visited.append(num)
                res[num] +=1

        sorted_l = dict(sorted(res.items(),key = lambda item:item[1],reverse = True)[:k])
        return list(sorted_l.keys())

        


        