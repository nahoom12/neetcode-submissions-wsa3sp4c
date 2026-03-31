class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        bucket = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            res[nums[i]] += 1
        for i,j in res.items():
            bucket[j].append(i)
        values = []
        for i in range(len(bucket)-1,-1,-1):
            for n in bucket[i]:
                values.append(n)
                if len(values) == k:
                    return values
        

        
        

        