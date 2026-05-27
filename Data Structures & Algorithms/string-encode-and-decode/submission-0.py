class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s+=str(len(i))
            s+='#'
            s+=i
        return s

    def decode(self, s: str) -> List[str]:
        l=[]
        a=''
        i=0
        while i<len(s):
            if s[i]!='#':
                a+=s[i]
                i+=1
            else:
                x=int(a)
                ds=s[i+1:i+x+1]
                l.append(ds)
                i+=x+1
                a=''
            
        return l

            