class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        lp=1
        
        for i in nums:
            l.append(lp)
            lp*=i

        rp=1
        for i in range(len(nums)-1,-1,-1):
            l[i]=l[i]*rp
            rp*=nums[i]
        
        return l