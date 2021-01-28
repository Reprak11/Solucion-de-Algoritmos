# https://codeforces.com/contest/431/problem/A
# Reprak11

a = list(map(int, input().strip().split()))
s = input()

print (sum([a[int(i)-1] for i in s]))