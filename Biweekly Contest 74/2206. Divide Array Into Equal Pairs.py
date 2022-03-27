'''
- Create map to store frequencies of each element.
- If any of the frequencies is odd then return false.
- If all frequencies are even then return true.
'''
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mapper = {}
        for i in nums:
            if i in mapper:
                mapper[i]+=1
            else:
                mapper[i] = 1
        for i in mapper:
            if mapper[i]%2==1:
                return False
        return True