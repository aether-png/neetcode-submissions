class Solution:
    def isValid(self, s: str) -> bool:
        m={')':'(','}':'{',']':'['}
        l=[]
        for i in s:
            if i in '({[':
                l.append(i)
            else:
                if not l or l[-1]!=m[i]:
                    return False
                l.pop()
            print(l)
        return len(l)==0


        