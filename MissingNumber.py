class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        total_sum = 0
        for i in range(0, len(nums)+1):
            total_sum += i

        for num in nums:
            total_sum -= num

        return total_sum
