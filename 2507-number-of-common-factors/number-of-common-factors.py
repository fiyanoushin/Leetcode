class Solution(object):
    def commonFactors(self, a, b):
      
        g = 1
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                g = i

        
        count = 0
        for i in range(1, g + 1):
            if g % i == 0:
                count += 1

        return count
