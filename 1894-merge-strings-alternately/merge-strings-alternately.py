class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
    
        # Use two pointers to traverse both strings
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            # Add a character from word1 if there's any left
            if i < len(word1):
                result.append(word1[i])
                i += 1
            # Add a character from word2 if there's any left
            if j < len(word2):
                result.append(word2[j])
                j += 1
        
        # Join the list into a string and return it
        return ''.join(result)
        