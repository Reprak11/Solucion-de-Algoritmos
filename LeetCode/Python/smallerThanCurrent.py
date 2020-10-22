# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Reprak11
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        cnt = 0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(nums[i]>nums[j]):
                    cnt = cnt+1
            output.append(cnt)
            cnt=0
        return output

if __name__ == "__main__":
    nums = input()[1:-1]
    nums=list(map(int, nums.split(",")))

    x=Solution()
    print(x.smallerNumbersThanCurrent2(nums))