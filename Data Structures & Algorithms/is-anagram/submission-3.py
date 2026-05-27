class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x={}
        y={}
        s = s.lower()
        t = t.lower()

        for i in s:
            if i in x:
                x[i]+=1
            else:
                x[i]=1
        for i in t:
            if i in y:
                y[i]+=1
            else:
                y[i]=1
        
        return x==y
