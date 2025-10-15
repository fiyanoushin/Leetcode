class Solution(object):
    def climbStairs(self, n):
        if n<=2:
            return n
        i,j=1,2
        for a in range(3,n+1):
            i,j=j,i+j
        return j
                


   
        
            

    
          



  

        