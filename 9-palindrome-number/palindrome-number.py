class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If the number is negative, it's not a palindrome
        if x < 0:
            return False
        
        # Store the original number
        original = x
        reversed_num = 0
        
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        # Compare the reversed number with the original number
        return original == reversed_num     