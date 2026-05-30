class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        final = []
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in res:
                res[sortedString] = []
            res[sortedString].append(string)
        for key in res:
            final.append(res[key])
        return final