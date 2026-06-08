class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k=0
        mc=0
        s=set(nums)
        for i in s:
            p=i
            if i-1 in s:
                continue
            
            k=1
            while p+1 in s:
                k+=1
                p=p+1
            mc=max(mc,k)
        return mc