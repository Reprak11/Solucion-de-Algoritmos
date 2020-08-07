# https://leetcode.com/problems/running-sum-of-1d-array/{}
# Reprak11
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accum=0
        result=[]
        for i in nums:
            accum += i
            result.append(accum)
        return result


if __name__ == "__main__":
    
    nums=input()[1:-1]
    nums=list(map(int,nums.split(",")))

    print(Solution.runningSum(Solution,nums))