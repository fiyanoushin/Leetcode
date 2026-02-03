class Solution(object):
    def commonChars(self, words):
        res=[]
        for w in words[0]:
            found=True
            for c in range(1,len(words)):
                if w not in words[c]:
                    found=False
                    break
                else:
                    words[c] = words[c].replace(w, "", 1)
            if  found:
                res.append(w)
        return res                

        