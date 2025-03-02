class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip any trailing spaces and split the string by spaces
        words = s.strip().split()
    
        # Return the length of the last word
        return len(words[-1])

        