class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        c=0
        for i in range(len(nums)):
            x=nums[i]
            c=target-x
            if c in m:
                a=m[c]
                return[a,i]
                
            else:
                m[x]=i