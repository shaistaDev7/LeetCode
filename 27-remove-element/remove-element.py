class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer1 = 0
        for pointer2 in range(len(nums)):
            if nums[pointer2] != val:
                nums[pointer1] = nums[pointer2]
                pointer1 += 1
        return pointer1
           
        