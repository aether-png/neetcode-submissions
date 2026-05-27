class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        x=[]

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            #i locked, now 2 sum 
            l=i+1
            r=len(nums)-1

            while l<r:
                s=nums[l]+nums[r]+nums[i]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else: # found triplets
                    x.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1

                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    
                    while l<r and nums[r]==nums[r+1]:
                        r-=1

        return x     
