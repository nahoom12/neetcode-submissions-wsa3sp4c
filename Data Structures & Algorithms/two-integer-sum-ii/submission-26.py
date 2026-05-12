class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers)-1
        r_list = []
        while first < last:
            sum_n = numbers[first] + numbers[last]
            if sum_n > target:
                last -=1
            elif sum_n < target:
                first +=1
            else:
                return [first+1,last+1]
                