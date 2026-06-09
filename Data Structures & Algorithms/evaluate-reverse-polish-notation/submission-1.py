class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i not in "+-/*":
                st.append(int(i))
            else:
                b=st.pop()
                a=st.pop()
                if i=="/":
                    x=int(a/b) #to fix for py negative
                elif i=="-":
                    x=a-b
                elif i=="+":
                    x=a+b
                else:
                    x=a*b  #2nd pop operand first
                st.append(x)
        return st[0]
