class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage ={}
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in storage:
                return [storage[compliment],i]
            storage[num] = i

        