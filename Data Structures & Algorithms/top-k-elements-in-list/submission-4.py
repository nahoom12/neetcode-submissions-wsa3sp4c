class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = {}
        freq = [[] for i in range(len(nums)+1)] 
        res =[]
        for num in nums:
            if num in storage:
                storage[num]+=1
            else:
                storage[num] = 1
        for n,c in storage.items():
            freq[c].append(n)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 
    





        
            