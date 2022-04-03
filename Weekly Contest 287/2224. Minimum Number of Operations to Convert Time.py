'''
- Convert current and correct time to minutes.
- Calculate difference between both times.
- Greedily use [60,15,5,1] minutes array to fill the difference.
'''
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ch,cm = list(map(int,current.split(':')))
        eh,em = list(map(int,correct.split(':')))
        cr = ch*60 + cm
        er = eh*60 + em
        diff = er-cr
        ans = 0
        for i in [60,15,5,1]:
            times = diff//i
            diff-=(times*i)
            ans+=times
        return ans