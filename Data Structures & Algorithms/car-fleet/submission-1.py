class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t=[]
        cars=list(zip(position,speed))
        cars.sort(reverse=True)  #coz 0 <= position[i] < target, so larger nearer
        for p,s in cars:
            t.append((target-p)/s)
        st=[]
        f=0

        for i in t:
            if not st :
                st.append(i)
                f+=1
            elif i<=st[-1]:
                pass  #same fleeet
        
            else:
                f+=1  #diff fleet too slow
                st.append(i)
        return f