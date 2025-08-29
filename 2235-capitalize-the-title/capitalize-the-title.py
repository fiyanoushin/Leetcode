class Solution:
    def capitalizeTitle(self, title: str) -> str:
        word=title.split()
        res=[]
        for ch in word:
            if len(ch)<=2:
                res.append(ch.lower())
            else:
                res.append(ch.capitalize()) 

        return " ".join(res)           

        
        