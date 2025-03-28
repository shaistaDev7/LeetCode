class Solution:
    def isValid(self, s: str) -> bool:
        brac_dict= {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []
        for char in s:
            if char in brac_dict:
                if stack and stack[-1] == brac_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack  else False
        