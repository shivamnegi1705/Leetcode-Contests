'''
- Using max heap, removing half of the topmost value.
- Increment count by 1.
'''
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        req = sum(nums)
        tot = req
        req = req/2
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        count = 0
        while len(nums)>0 and tot>req:
            cur = -heapq.heappop(nums)
            nex = cur/2
            diff = cur-nex
            tot-=diff
            if nex>0:
                heapq.heappush(nums,-nex)
            count+=1
        return count