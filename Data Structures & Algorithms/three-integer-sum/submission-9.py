class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_l = sorted(nums)
        res = []
        for i,a in enumerate(nums_l):
            if i > 0 and nums_l[i-1] == a:
                continue
            l,r = i + 1,len(nums_l) - 1
            while l < r:
                threeSum = a + nums_l[l] + nums_l[r]
                if threeSum < 0:
                    l +=1
                elif threeSum > 0:
                    r -=1
                else:
                    res.append([a,nums_l[l],nums_l[r]])
                    l += 1
                    while  nums_l[l] == nums_l[l-1] and l < r:
                        l +=1
        return res
                
                





        
    

                

       



                
            
        