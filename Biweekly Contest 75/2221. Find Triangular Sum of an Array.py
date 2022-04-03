'''
1 <= nums.length <= 1000
- Process will repeat for n-1 times. where n = size of nums array.
- Traverse nums array each time and calculate (nums[i]+nums[i+1])%10, 
  and create new nums array with size less than 1 than previous.
'''
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            nex = []
            for j in range(len(nums)-1):
                nex.append((nums[j]+nums[j+1])%10)
            nums = nex[::]
        return nums[0]