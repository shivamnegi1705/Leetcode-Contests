'''
- First half part of palindrome is ordered.
Example:- length = 8
First half part => 1000,1001,1002,1003....
so, First half of ith palindrome = pow(10,(intLength//2)-1)+(i-1)
- Second half part = reverse of first part
- If first half + second half > intLength then return -1.
'''
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        n = len(queries)
        k = intLength//2
        ans = [-1 for i in range(n)]
        if intLength%2==0:
            base = pow(10,k-1)
            index = 0
            for i in queries:
                half = i-1
                num = base+half
                res = str(num)+str(num)[-1::-1]
                res = int(res)
                if len(str(res))==intLength:
                    ans[index] = res
                index+=1
        else:
            base = pow(10,k)
            index = 0
            for i in queries:
                half = i-1
                num = base+half
                num = str(num)
                res = num+num[:k:][-1::-1]
                res = int(res)
                if len(str(res))==intLength:
                    ans[index] = res
                index+=1
        return ans