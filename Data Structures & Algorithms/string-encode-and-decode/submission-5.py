class Solution:

    def encode(self, strs: List[str]) -> str:
        s1=""
        for i in strs:
            s1=s1+str(len(i))+"#"+i
        return s1

    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        t=""
        while i<len(s):
            if s[i]!="#":
                t+=s[i]
                i+=1

            else:
                n=int(t)
                w=s[i+1:i+n+1]
                l.append(w)
                i+=1+n
                t=""

        return l