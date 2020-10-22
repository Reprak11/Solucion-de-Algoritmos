# https://leetcode.com/problems/jewels-and-stones/
# Reprak11
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        output=0
        for i in S:
            if (i in J):
                output=output+1
        return output

if __name__ == "__main__":
    J=input()
    S=input()
    x=Solution()
    print(x.numJewelsInStones(J,S))