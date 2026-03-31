class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = defaultdict(list)
        for text in strs:
            key = ''.join(sorted(text))
            storage[key].append(text)
        my_list = list(storage.values())
        return my_list


            


        