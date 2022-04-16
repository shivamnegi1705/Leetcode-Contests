'''
- Using dis variable to keep track of closest number be it positive or negative.
- Using ans variable to store the largest value.
'''
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dis = 10**10
        ans = -10**10
        for i in nums:
            num = abs(i)
            if num<dis:
                dis = num
                ans = i
            elif num==dis:
                ans = max(ans,i)
        return ans