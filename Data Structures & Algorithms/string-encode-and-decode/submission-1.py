class Solution:

    def encode(self, strs: List[str]) -> str:
        a=''
        for i in strs:
            n=len(i)
            a+=str(n)
            a+='#'
            a+=i
        return(a)

    def decode(self, s: str) -> List[str]:
        l=[]
        n=''
        i=0
        while i<(len(s)):
            if s[i]!='#':
                n+=s[i]
                i+=1

            else:
                m=int(n)
                l.append(s[i+1:i+m+1])
                i+=m+1
                n=''
        return(l)

