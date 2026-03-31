class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage ={}
        for i in range(len(nums)):
            if(nums[i] in storage):
                return True
            storage[nums[i]] = i
        return False

            