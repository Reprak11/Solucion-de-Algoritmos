# https://leetcode.com/problems/two-sum/
# Reprak11

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictio = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in dictio:
                return[dictio[diff],i]
            dictio[j]=i
        return 

dato1= input()[1:-1]
nums=list(map(int,dato1.split(",")))

target=int(input())

print(Solution.twoSum(Solution,nums,target))





