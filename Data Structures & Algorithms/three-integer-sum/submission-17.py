class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_num = sorted(nums)
        res_l = []
        for i in range(len(sort_num)):
            if i > 0 and sort_num[i-1] == sort_num[i]:
                continue
            first = i + 1
            last = len(sort_num) - 1
            while first < last:
                sum_z = sort_num[i] + sort_num[first] + sort_num[last]
                if sum_z > 0:
                    last-=1
                elif sum_z < 0:
                    first += 1
                else:
                    found_z = [sort_num[i],sort_num[first],sort_num[last]]
                    res_l.append(found_z)
                    first +=1
                    while  sort_num[first] == sort_num[first - 1] and first < last:
                        first += 1
        return res_l


        