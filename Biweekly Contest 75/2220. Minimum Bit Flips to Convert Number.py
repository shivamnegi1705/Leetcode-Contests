'''
Check all the bits till 32. If bits differ in 'start' and 'goal' then increase ans by 1.
'''
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cur = 1
        ans = 0
        for i in range(32):
            if start&cur != goal&cur:
                ans+=1
            cur = cur*2
        return ans