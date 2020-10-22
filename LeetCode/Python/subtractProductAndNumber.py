# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Reprak11

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        producto=1
        suma=0
        for i in (str(n)):
            producto *=  int(i)
            suma += int(i)
        return producto-suma

if __name__ == "__main__":
    n = int(input())
    x=Solution()
    print(x.subtractProductAndSum(n))