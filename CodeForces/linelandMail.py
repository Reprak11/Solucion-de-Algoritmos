# https://codeforces.com/contest/567/problem/A
# Reprak11

n = int(input())
x = list(map(int,input().split()))

for i in range(n):
    xmax=max(abs(x[i]-x[0]), abs(x[n-1]-x[i]))
    if i == 0:
        xmin=abs(x[i]-x[i+1])
    if i == n-1:
        xmin=abs(x[i]-x[i-1])
    else:
        xmin=min(abs(x[i]-x[i+1]), abs(x[i]-x[i-1]))
    print(xmin,xmax)
    