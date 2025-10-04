class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        extra_candy=max(candies)
        res=[]
        for i in candies:
            if i+extraCandies>=extra_candy:
                res.append(True)
            else:
                res.append(False) 
        return res       

            
        