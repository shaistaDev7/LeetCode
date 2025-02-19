class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dic_opt={"--X": -1,"X--":-1,"++X":1,"X++":1}
        result=0
        for i in operations:
            result+=dic_opt[i]
        return result

        