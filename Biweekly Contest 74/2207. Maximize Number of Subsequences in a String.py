'''
pattern is of 2 length
- Case 1: pattern[0]==pattern[1]
  a = count of pattern[0]
  text = abaaba
  pattern = aa
  count of 'a' = 4. we will add one 'a' at start or at end.
  resultant text     = a a b a a b a
  contrib. of each 'a' = 4 3   2 1    --> 10 = (a*(a+1))/2

- Case 2: pattern[0]!=pattern[1]
  a = count of pattern[0]
  b = count of pattern[1]
  text = aabaab
  pattern = ab

  - Case 2(a):- Adding 'a' in start of text 
    resultant text = a a a b a a b
    contrib of 'a' = 2 2 2   1 1   --> 8

  - Case 2(a):- Adding 'b' in end of text 
    resultant text = a a b a a b b
    contrib of 'a' = 3 3   2 2     --> 10

  Taking max of both cases.
'''
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a,b = 0,0
        for i in text:
            if i==pattern[0]:
                a+=1
            if i==pattern[1]:
                b+=1
        if pattern[0]==pattern[1]:
            return (a*(a+1))//2
        if a==0:
            if b==0:
                return 0
            else:
                return b
        else:
            if b==0:
                return a
            else:
                rem = b
                ans = 0
                ta = rem
                for i in text:
                    if i==pattern[0]:
                        ta+=rem
                    elif i==pattern[1]:
                        rem-=1
                ans = max(ans,ta)
                rem = b+1
                ta = 0
                for i in text:
                    if i==pattern[0]:
                        ta+=rem
                    elif i==pattern[1]:
                        rem-=1
                ans = max(ans,ta)
                return ans