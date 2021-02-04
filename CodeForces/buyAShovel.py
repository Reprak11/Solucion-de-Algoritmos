# http://codeforces.com/contest/732/problem/A
# Reprak11

k, r = list(map(int, input().strip().split()))

i=1
while (k*i%10 != 0 and (k*i)%10 != r):
    i+=1

print(i)