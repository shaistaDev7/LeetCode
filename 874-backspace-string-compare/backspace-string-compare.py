class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans1=[]
        ans2=[]
        for i in s:
            if i != "#":
                ans1.append(i)
            elif ans1:
                ans1.pop()

        for i in t:
            if i != "#":
                ans2.append(i)
            elif ans2:
                ans2.pop()
        return ans1==ans2