class Solution(object):
    def findDisappearedNumbers(self, nums):
        res=[]
        n=len(nums)
        num=set(nums)
        for i in range(1,n+1):
            if i not in num:
                res.append(i)
             
        return res    
              
    
        
        