# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Reprak11

class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while (num > 0):
            if (num%2 == 0):
                num = num/2
            else:
                num=num-1
            steps = steps+1
        return steps

if __name__ == "__main__":
    num=int(input())
    x=Solution()
    print(x.numberOfSteps(num))