class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stack = []

        i = 0
        while i < len(nums):
            if stack and stack[-1] > 0 and nums[i] < 0:
                # collision -> yes
                if abs(stack[-1]) > abs(nums[i]):
                    i = i + 1
                elif abs(stack[-1]) < abs(nums[i]):
                    stack.pop()

                    continue
                else:
                    stack.pop()
                    i = i + 1
            else:
                stack.append(nums[i])
                i = i + 1
        print(stack)

        return stack