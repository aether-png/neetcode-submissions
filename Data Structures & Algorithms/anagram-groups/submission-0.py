class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m={}
        for i in strs:
            x="".join(sorted(i))
            if x in m:
                (m[x]).append(i)
            else:
                m[x]=[i]

        l=[]
        for i in m.values():
            l.append(i)
        return l
        
        