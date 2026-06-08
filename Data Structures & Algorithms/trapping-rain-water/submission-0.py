class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        w=0
        lm=height[l]
        rm=height[r]

        while l<r:
            lm=max(lm,height[l])
            rm=max(rm,height[r])

            if lm>rm:
                w+=rm-height[r]
                r-=1
            else:
                w+=lm-height[l]
                l+=1

        return w
