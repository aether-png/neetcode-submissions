class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a={}
        for i in strs:
            b="".join(sorted(i))
            print(b)
            if b in a:
                a[b].append(i)
            else:
                a[b]=[i]
            
        x=list(a.values())
        return x