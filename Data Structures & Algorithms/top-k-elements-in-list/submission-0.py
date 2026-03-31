class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = {}
        for num in nums:
            if num in storage:
                storage[num]+=1
            else:
                storage[num] = 1
        vals=sorted(storage,key = storage.get,reverse = True)[:k]
        return vals
            