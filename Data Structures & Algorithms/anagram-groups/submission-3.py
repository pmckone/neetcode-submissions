class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        final = []
        for strings in strs:
            sortedStrs= "".join(sorted(strings))
            if sortedStrs not in res:
                res[sortedStrs] = []
            res[sortedStrs].append(strings)
        for key in res:
            final.append(res[key])
        return final