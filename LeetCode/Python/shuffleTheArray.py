# https://leetcode.com/problems/shuffle-the-array/
# Reprak11
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        salida=[]
        for i in range (0,n):
            salida.append(nums[i])
            salida.append(nums[i+n])
        return salida


if __name__ == "__main__":
    nums = input()[1:-1]
    nums = list(map(int,nums.split(",")))
    n = int(input())
    print(Solution.shuffle(Solution,nums,n))