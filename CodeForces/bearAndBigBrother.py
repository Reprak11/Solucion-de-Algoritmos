# https://codeforces.com/contest/791/problem/A
# Reprak11

a, b = map(int, input().strip().split())

years = 0

while (a <= b):
    a *= 3
    b *= 2
    years += 1

print(years)