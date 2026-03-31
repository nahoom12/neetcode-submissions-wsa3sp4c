class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = defaultdict(int)
        numset = set(nums)
        if nums == []:
            return 0
        for num in numset:
            if num in res:
                continue
            x = num
            if num - 1 not in nums and num + 1 in nums:
                res[x] += 2
                num = num + 1
                while num + 1 in nums:
                    res[x] +=1
                    num = num + 1
            else:
                res[num] = 1
        return max(res.values())

                 

              

 




        