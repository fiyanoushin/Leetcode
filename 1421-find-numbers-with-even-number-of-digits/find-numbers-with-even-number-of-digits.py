class Solution(object):
    def findNumbers(self, nums):
        count=0
        for num in nums:
            n=str(num)
            if len(n)%2==0:
                count +=1
        return count    

       