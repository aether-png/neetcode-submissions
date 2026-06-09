class MinStack:

    def __init__(self):
        self.ms=[]     #memory stays in self, so self._ has to be used
        self.st=[]
        

    def push(self, val: int) -> None:
        self.st.append(val)
        
        if not self.ms:   #empty stack condtion, so element appended without min
            self.ms.append(val)
        else:
            self.ms.append(min(self.ms[-1],val))
        

    def pop(self) -> None:
        self.st.pop()
        self.ms.pop()

    def top(self) -> int:
        x=self.st[-1]
        return x

    def getMin(self) -> int:
        x=self.ms[-1]
        return x
        
