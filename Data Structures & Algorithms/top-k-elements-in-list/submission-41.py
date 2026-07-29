class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        index_list = [[] for i in range(len(nums) + 1)]
        res = {}
        top = []
        for i in range(len(nums)):
            if nums[i] in res:
                res[nums[i]] += 1
            else:
                res[nums[i]] = 1
        for num,count in res.items():
            index_list[count].append(num)
        for j in range(len(nums),-1,-1):
                for num in index_list[j]:
                    top.append(num)
                    if len(top) == k:
                        return top
       
        