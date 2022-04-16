'''
Let's say ways = maximum count of pens we can buy using total amount
Then for each way for pens from 0,1,2,3,....ways 
we can find out number of ways for pencils by calculating count of pencils for remaining amount.
'''
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ways = total//cost1
        ans = 0
        for i in range(ways+1):
            rem = total - (i*cost1)
            count = rem//cost2
            ans+=(count+1)
        return ans