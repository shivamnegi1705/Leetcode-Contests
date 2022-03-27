'''
- Idea is to traverse the nums array and add element in the ans array 
- If last index is odd or even but ans[-1]!=current value of nums
- We will increment removed value count if last index of ans is even and ans[-1]==current value
- If final array is of odd size we will return (removed+1) count else removed count.
'''
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans = []
        index = -1
        removed = 0
        for i in nums:
            if ans==[]:
                ans.append(i)
                index+=1
            else:
                if index%2==0:
                    if ans[-1]!=i:
                        ans.append(i)
                        index+=1
                    else:
                        removed+=1
                else:
                    ans.append(i)
                    index+=1
        return removed+(len(ans)%2)