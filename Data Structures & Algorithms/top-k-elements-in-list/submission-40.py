class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            res[num] +=1
        for num,count in res.items():
            freq[count].append(num)
        return_list = []
        for i in range(len(freq)-1,-1,-1):
            for number in freq[i]:
                return_list.append(number)
                if len(return_list) == k:
                    return return_list

