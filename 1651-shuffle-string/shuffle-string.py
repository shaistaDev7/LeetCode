class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic={}
        res=""
        for i in range(len(s)):
            dic[indices[i]]=s[i]
        indices.sort()
        for i in indices:
            res+=dic[i]
        return res
        