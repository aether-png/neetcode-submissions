class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m={}
        for w in strs:
            k="".join(sorted(w))
            if k not in m:
                m[k]=[]
            m[k].append(w)

        l=[]

        return(list(m.values()))
        
