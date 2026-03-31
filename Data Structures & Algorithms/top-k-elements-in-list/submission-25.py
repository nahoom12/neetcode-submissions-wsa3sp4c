class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        freq_list = [[] for i in range(len(nums) + 1)]
        for num in nums:
            res[num] += 1
        for number,freq in res.items():
            freq_list[freq].append(number)
        resl = []
        for i in range(len(freq_list)-1,0,-1):
            for n in freq_list[i]:
                resl.append(n)
                if len(resl) == k:
                    return resl
                
        