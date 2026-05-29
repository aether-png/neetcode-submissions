from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        b=[[] for _ in range(len(nums)+1)]

        for n in freq:
            b[freq[n]].append(n)

        res=[]

        for i in range(len(b)-1,0,-1):
            for j in b[i]:
                res.append(j)
                if len(res)==k:
                    return res
               
            

