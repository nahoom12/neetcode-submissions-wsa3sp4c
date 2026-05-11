class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        res = defaultdict(int)
        check = defaultdict(list)
        if nums == []:
            return 0
        for num in numbers:
            if num in res:
                continue
            if num - 1 in numbers:
                count = 2
                second = num - 1
                while second - 1 in numbers:
                    second = second - 1
                    count += 1
                if not res:
                    res[second] = count
                if count >= max(res.values()):
                    res[second]= count

                else:
                    continue        
            else:
                res[num] = 1
        return max(res.values())
        
                


        