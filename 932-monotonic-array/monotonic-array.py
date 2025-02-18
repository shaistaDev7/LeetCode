class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # def isincreasing(nums):
        #     for i in range(nums.length-1):
        #         if num[i]<=num[i+1]:
        #             return true
        #     return false

        # def isincreasing(nums):
        #     for i in range(nums.length-1):
        #         if num[i]>=num[i+1]:
        #             return true
        #     return false  
        increasing = decreasing = True
        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:

                decreasing = False
            elif nums[i] < nums[i - 1]:
                increasing = False
    
        return increasing or decreasing 