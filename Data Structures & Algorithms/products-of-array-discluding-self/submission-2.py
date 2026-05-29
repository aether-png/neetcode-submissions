class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]* len(nums)
        lp=1
        rp=1
        for i in range(len(nums)):
            l[i]=lp
            lp=lp*nums[i]
            
        
        for i in range(len(nums)-1,-1,-1):
            l[i]*=rp
            rp*=nums[i]
        return l


