class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        set_n = set(numbers)
        for i in range(len(numbers)):
            res[numbers[i]] = i + 1
        for i in range(len(numbers)):
            if target - numbers[i] in set_n:
                return [i + 1,res[target - numbers[i]]]
        


        