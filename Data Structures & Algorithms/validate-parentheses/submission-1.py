class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        m={
            "}":"{",
            ")":"(",
            "]":"["
        }
        for ch in s:
            
            if ch in "({[":
                st.append(ch)
            
            elif ch in ")]}":
                if len(st)==0:
                    return False
                else:
                    if st[-1]==m[ch]:
                        st.pop()
                    else:
                        return False

        if len(st)==0:
            return True
        else:
            return False 
