class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        final = []
        for strings in strs:
            sorted_str = "".join(sorted(strings))
            if sorted_str not in res:
                res[sorted_str] = []
            res[sorted_str].append(strings)
        
        for key in res:
            final.append(res[key])
                
        return final
