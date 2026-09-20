class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(1,len(nums)):
            value = nums[i-1] ^ nums[i]
            print(value)
            if value == 0 :
                return True 
        return False
        