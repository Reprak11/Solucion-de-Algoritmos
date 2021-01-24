# https://codeforces.com/contest/344/problem/A
# Reprak11

n=int(input())

count=0
temp=''
for i in range(n):
    magnet=input()
    count += 1 if magnet != temp else 0
    temp = magnet

print(count)