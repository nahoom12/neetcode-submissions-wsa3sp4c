class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for words in strs:
            alphabet_index = [0]*26
            for c in words:
                alphabet_index[ord("z") - ord(c)] += 1
            res[tuple(alphabet_index)].append(words)
        return list(res.values())
            

            
        