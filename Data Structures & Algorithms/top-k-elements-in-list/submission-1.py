class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m={}
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        n=len(nums)
        l=[[] for i in range(n+1)]
        
        for i in m:
                f=m[i]
                l[f].append(i)
        r=[] 
        for i in range(n,0,-1):
            for j in l[i]:
                r.append(j)
                if len(r)==k:
                    return r
                    

        
