'''
For each edge, let's consider it the edge between (B, C), and try to make an optimal quadruplet (A, B, C, D) out of the neighbors of B and C.
We get A from B's neighbors, and D from C's neighbors.

Notice that we don't need to store information of all the neighbors of a node because we only need the node with the largest score, thus saving 3 neighboring nodes is enough.

'''
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        graph = [[] for i in range(n)]
        for i in edges:
            x,y = i
            total = scores[x]+scores[y]
            graph[x].append([total,y])
            graph[y].append([total,x])
        ind = 0
        for i in graph:
            temp = graph[ind]
            temp.sort(reverse=True)
            temp = temp[:3:]
            graph[ind] = temp
            ind+=1
        ans = -1
        for i in edges:
            x,y = i
            left = graph[x]
            right = graph[y]
            for (wt1,j) in left:
                for (wt2,k) in right:
                    if j==k:
                        continue
                    if j not in i and k not in i:
                        ans = max(ans,scores[x]+scores[y]+scores[j]+scores[k])
        return ans