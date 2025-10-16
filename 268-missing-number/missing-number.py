class Solution(object):
    def missingNumber(self, nums):
        res=0
        n=len(nums)
        total_sum=sum(range(0,n+1))
        total=sum(nums)
        res=total_sum-total
        return res

      


        