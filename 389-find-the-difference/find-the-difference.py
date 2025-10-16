class Solution(object):
    def findTheDifference(self, s, t):
        s1=sorted(s)
        s2=sorted(t)
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return s2[i]

           
        return s2[-1]    
      
        
           
       
      
        