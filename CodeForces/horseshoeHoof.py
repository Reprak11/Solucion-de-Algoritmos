# https://codeforces.com/contest/228/problem/A
# Reprak11

a = list(map(int, input().strip().split()))

print(len(a)-len(set(a)))