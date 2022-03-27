'''
- Create map of unique values for nums1 and nums2 arrays.
- Traverse each map and check if the value the other map.
- If the value is not present then add that value in the ans array.
'''
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[],[]]
        mapper1,mapper2 = {},{}
        for i in nums1:
            mapper1[i] = 1
        for i in nums2:
            mapper2[i] = 1
        for i in mapper1:
            if i not in mapper2:
                ans[0].append(i)
        for i in mapper2:
            if i not in mapper1:
                ans[1].append(i)
        return ans