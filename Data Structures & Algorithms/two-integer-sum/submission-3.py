class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            y=nums[i]
            x=target-y
            if x in a:
                return[a[x],i]
            else:
                a[nums[i]]=i
        
     