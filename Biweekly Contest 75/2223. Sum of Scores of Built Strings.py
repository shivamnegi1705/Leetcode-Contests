'''
Using z-algorithm add all the values of z_array to get the ans.
z[0] = n
'''
class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0 for i in range(n)]
        l,r = 0,0
        for i in range(1,n):
            if i<=r:
                z[i] = min(r-i+1,z[i-l])
            while (i+z[i] < n) and s[z[i]] == s[i+z[i]]:
                z[i]+=1
            if i+z[i]-1>r:
                l = i
                r = i+z[i]-1
        z[0] = n
        return sum(z)