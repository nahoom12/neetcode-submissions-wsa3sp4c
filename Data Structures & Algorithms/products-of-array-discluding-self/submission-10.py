class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        x = 1
        listp = []
        #listn = []
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                #listn.append(nums[i])
                zero_count+=1
                product = 0
            else:
                product = product * nums[i]
        if zero_count == 1:
            for num in nums:
                if num !=0:
                    x = num *x
        for num in nums:
            if num !=0:
                divided = product//num
                listp.append(divided)
            elif num == 0 and zero_count == 1:
                listp.append(x)
            elif zero_count >=2:
                listp = [0]*(len(nums))
                return listp
        return listp
