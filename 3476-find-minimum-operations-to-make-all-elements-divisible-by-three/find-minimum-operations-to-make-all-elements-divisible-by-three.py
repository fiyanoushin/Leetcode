class Solution(object):
    def minimumOperations(self, nums):
       count=0
       for num in nums:
        if num%3!=0:
            count+=1
       return count     
                    

      




       