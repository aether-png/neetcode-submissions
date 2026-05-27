class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        p=1
        for i in nums:
            left.append(p)
            p*=i
        
        
        
        rp=1
        for i in range(len(nums)-1,-1,-1):
            left[i]=rp*left[i]
            rp*=nums[i]
        
        return left
