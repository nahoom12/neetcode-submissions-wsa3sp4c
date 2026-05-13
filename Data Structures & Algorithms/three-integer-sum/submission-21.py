class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_num = sorted(nums)
        res_l = []
        for i in range(len(sort_num)):
            if i > 0 and sort_num[i-1] == sort_num[i]:
                continue
            l = i + 1
            r = len(sort_num) - 1
            while l < r:
                sum_z = sort_num[i] + sort_num[l] + sort_num[r]
                if  sum_z > 0:
                    r -= 1
                elif sum_z < 0:
                    l += 1
                else:
                    res_l.append([sort_num[i],sort_num[l],sort_num[r]])
                    l += 1
                    while sort_num[l] == sort_num[l - 1] and l < r:
                        l += 1
        return res_l

       


        