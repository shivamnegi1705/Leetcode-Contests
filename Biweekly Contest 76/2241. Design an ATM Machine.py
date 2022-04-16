class ATM:

    def __init__(self):
        self.money = [20,50,100,200,500]
        self.count = {}
        for i in range(5):
            self.count[self.money[i]] = 0

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.count[self.money[i]]+= banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        rem = amount
        ind = -1
        ans = [0 for i in range(5)]
        for i in range(5):
            cnt = self.count[self.money[ind]]
            if cnt > 0:
                x = rem//self.money[ind]
                ans[ind] = min(x,cnt)
                rem-=(ans[ind]*self.money[ind])
            ind-=1
        if rem!=0:
            return [-1]
        else:
            for i in range(5):
                self.count[self.money[i]]-=ans[i]
            return ans
                


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)