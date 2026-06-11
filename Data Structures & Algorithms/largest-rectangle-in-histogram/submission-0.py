class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ma=0
        st=[]
        heights.append(0)

        for i in range(len(heights)):
            
            while st and heights[i]<heights[st[-1]]:
                x=st.pop()
                if st:
                    a=heights[x]*(i-st[-1]-1)
                else:
                    a=heights[x]*(i)
                ma=max(a,ma)
            
            st.append(i)
        return ma
