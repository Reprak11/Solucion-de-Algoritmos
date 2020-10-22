# https://leetcode.com/problems/shuffle-string/
# Reprak11
from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=[]
        for i in range(0,len(s)):
            res.append(s[indices.index(i)])
        return "".join(res) 


if __name__ == "__main__":
    s=input()
    
    indices = input()[1:-1]
    indices=list(map(int,indices.split(",")))

    x=Solution()
    print(x.restoreString(s,indices))