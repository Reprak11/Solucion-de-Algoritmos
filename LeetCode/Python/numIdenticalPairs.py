# https://leetcode.com/problems/number-of-good-pairs/
# Reprak11

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if((nums[i] == nums[j])):
                    print(str(i)+" "+str(j))
                    cnt=cnt+1
        return cnt

if __name__ == "__main__":
    nums = input()[1:-1]
    nums = list(map(int, nums.split(",")))
    x=Solution()
    print(x.numIdenticalPairs(nums))