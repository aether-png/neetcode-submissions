class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        A=0

        while l<r:
            w=r-l
            h=min(heights[r],heights[l])
            a=h*w
            if a>A:
                A=a
            
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
            
        return A
