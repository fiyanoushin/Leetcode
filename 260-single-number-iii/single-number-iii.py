class Solution(object):
    def singleNumber(self, nums):
        res=[]
        for n in nums:
            if nums.count(n)==1:
                res.append(n)
        return res        

        
        