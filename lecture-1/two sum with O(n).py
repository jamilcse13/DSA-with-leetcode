class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        length = len(nums)
        
        for i in range(length):
            diff = target - nums[i]
            if diff in hashMap:
                return [i, hashMap[diff]]
            hashMap[nums[i]] = i
            
            
            
#Input: twoSum([2,7,11,15], 9)
#Output: [0,1]
