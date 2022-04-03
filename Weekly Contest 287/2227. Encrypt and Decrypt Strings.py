'''
- Create dict. to map keys[i] to values[i]
- Create dict. to map values[i] to list(keys[i])
- Encrypt each dictionary word and keep count in another map.
'''
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.mapper1 = {}
        self.mapper2 = {}
        self.mapper3 = defaultdict(int)
        self.n = len(keys)
        
        for i in range(self.n):
            self.mapper1[keys[i]] = values[i]
        for i in range(self.n):
            if values[i] in self.mapper2:
                self.mapper2[values[i]].append(keys[i])
            else:
                self.mapper2[values[i]] = [keys[i]]
        for i in dictionary:
            cur = ''
            for j in i:
                cur+=self.mapper1[j]
            self.mapper3[cur]+=1

    def encrypt(self, word1: str) -> str:
        cur = ''
        for i in word1:
            cur+=self.mapper1[i]
        return cur

    def decrypt(self, word2: str) -> int:
        return self.mapper3[word2]


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)