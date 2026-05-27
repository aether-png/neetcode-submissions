class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m=set()
        length=0

        for i in nums:
            if i not in m:
                m.add(i)
        
        for j in m:
            if j-1 not in m:
                pointer=j
                x=1

                while pointer + 1 in m:
                    pointer+=1
                    x+=1

                length=max(length,x)
        return length

