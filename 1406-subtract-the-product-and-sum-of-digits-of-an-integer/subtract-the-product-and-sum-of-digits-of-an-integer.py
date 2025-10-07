class Solution(object):
    def subtractProductAndSum(self, n):
        prod=1
        s=0
        nums=str(n)
        for n in nums:
            d=int(n)
            prod *=d
            s +=d
        return prod-s    

        
        