class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         return len(set(nums))!=len(nums)

        #nums.sort()
        ##for i in range (1,len(nums)):
            #if nums[i]==nums[i-1]:
             #   return True
            #return False
