class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Pointer for the position of the next non-zero element
        non_zero_position = 0

        # Move non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_position] = nums[i]
                non_zero_position += 1

        # Fill the rest of the array with zeros
        for i in range(non_zero_position, len(nums)):
            nums[i] = 0
        
        