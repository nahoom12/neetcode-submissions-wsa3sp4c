class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        start = 0
        end = len(numbers) - 1
        while start <= end:
            if target - numbers[start] == numbers[end]:
                return [start + 1, end + 1]
            if target - numbers[start] in res:
                if res[target- numbers[start]] > start + 1:
                    return [start + 1,res[target- numbers[start]]]
                else:
                    return [res[target- numbers[start]],start + 1]
            if target - numbers[end] in res:
                if res[target- numbers[end]] > end + 1:
                    return [end + 1,res[target- numbers[end]]]
                else:
                    return [res[target- numbers[end]],end + 1]
            res[numbers[start]] = start + 1
            res[numbers[end]] = end + 1
            start += 1
            end -= 1

        


        