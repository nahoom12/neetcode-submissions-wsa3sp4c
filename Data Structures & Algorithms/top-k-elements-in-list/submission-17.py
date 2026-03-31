class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            res[num] += 1
        for n,f in res.items():
            freq[f].append(n)
        resl = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                resl.append(n)
                if(len(resl) == k):
                    return resl

                

            


        


        