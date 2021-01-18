# http://codeforces.com/contest/231/problem/A
# Reprak11

n = int(input())
tests = []

for i in range(n):
    tests.append(sum(list(map(int, input().strip().split()))))

print(sum(i>1 for i in tests))