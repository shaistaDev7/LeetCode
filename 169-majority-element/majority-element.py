from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        # Phase 1: Find the potential candidate
        for n in nums:
            if count == 0:
                candidate = n
            count += (1 if n == candidate else -1)
        
        # Phase 2: Verify if the candidate is the majority element
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        else:
            return -1
