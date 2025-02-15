class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
         # Convert both lists to sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection of both sets
        result = list(set1 & set2)
        
        return result
        