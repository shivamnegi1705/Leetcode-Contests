'''
- We can do Binary search on number of candies a children can get.
- We will prove if we can allocate x candies to k children using solve method.
'''
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 0
        r = 10**18
        
        def solve(mid):
            cnt = 0
            for i in candies:
                cnt+=i//mid
            return cnt>=k
        
        while l<r:
            mid = (l+r)//2
            can = solve(mid)
            if can==True:
                l = mid
            else:
                r = mid
            if r-l==1:
                break
        if solve(r)==True:
            return r
        return l