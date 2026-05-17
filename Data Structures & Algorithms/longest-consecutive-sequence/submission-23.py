class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        m_lookup = defaultdict(int)
        count  = 0
        if nums == []:
            return count
        for num in numbers:
            if num in m_lookup:
                continue
            x = num
            if num + 1 in numbers and num - 1 not in numbers:
                count += 2
                num = num + 1
                while num + 1 in numbers:
                    count += 1
                    num = num + 1
                m_lookup[x] = count
            else:
                m_lookup[num] = 1
            count = 0
        return max(m_lookup.values())


                
            



        