class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      start  = 0
      end = len(numbers) - 1
      while start < end:
        temp_s  =  numbers[start] + numbers[end]
        if temp_s > target:
            end -= 1
        elif temp_s < target:
            start += 1
        else:
            return [start + 1,end + 1]
        


        