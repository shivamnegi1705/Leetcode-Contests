'''
- Create map for count of win and loss for players.
- Traverse win map and check if that player is not in loss. Add it in ans[0]
- Traverse loss map if player has losses equals to 1. Add it in ans[1].
- Sort ans[0] and ans[1].
'''
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win,loss = defaultdict(int),defaultdict(int)
        for i in matches:
            win[i[0]]+=1
            loss[i[1]]+=1
        ans = [set(),set()]
        for i in win:
            if loss[i]==0:
                ans[0].add(i)
        for i in loss:
            if loss[i]==1:
                ans[1].add(i)
        a,b = list(ans[0]),list(ans[1])
        if a!=[]:
            a.sort()
        if b!=[]:
            b.sort()
        return [a,b]