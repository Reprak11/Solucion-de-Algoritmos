# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Reprak11
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output=[]
        for i in candies:
            if(i+extraCandies >= max(candies)):
                output.append(True)
            else:
                output.append(False)
        return output
    def kidsWithCandies2(self, candies: List[int], extraCandies: int) -> List[bool]:
        output=map(lambda x: (x+extraCandies) >= max(candies) ,candies)
        return list(output)



if __name__ == "__main__":
    #Input de dulces
    candies=input()[1:-1]
    candies=list(map(int,candies.split(",")))
    
    #Input de dulces extras
    extraCandies=int(input())

    x=Solution()
    print(x.kidsWithCandies2(candies,extraCandies))