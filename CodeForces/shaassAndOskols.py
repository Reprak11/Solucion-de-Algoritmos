# http://codeforces.com/contest/294/problem/A
# Reprak11

n = int(input())
a = list(map(int, input().strip().split()))

m = int(input())

for i in range (m):
    shoot=list(map(int, input().strip().split()))
    l = shoot[1]-1
    r = a[shoot[0]-1]-shoot[1]
    if(shoot[0] != 1):
        a[shoot[0]-2] += l
    if(shoot[0] != n):
        a[shoot[0]] += r
    a[shoot[0]-1] = 0

[print(i) for i in a]