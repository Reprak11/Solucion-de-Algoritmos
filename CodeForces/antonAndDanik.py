# https://codeforces.com/contest/734/problem/A
# Reprak11

n = int(input())
winRecord = list(input())

anton=0
danik=0

for i in winRecord:
    if i == 'D':
        danik += 1
    else:
        anton += 1

if anton > danik:
    print("Anton")
elif anton < danik:
    print("Danik")
else:
    print("Friendship")