# https://codeforces.com/contest/490/problem/A
# Reprak11

n = int(input())
t = input().strip().split()

counter = 0
teams=[]

while('1' in t and '2' in t and '3' in t):
    counter += 1
    team = [str(t.index('1')+1),str(t.index('2')+1),str(t.index('3')+1)]
    t[(t.index('1'))]=""
    t[(t.index('2'))]=""
    t[(t.index('3'))]=""
    teams.append(team)
print(counter)
[print(" ".join(team)) for team in teams]
    