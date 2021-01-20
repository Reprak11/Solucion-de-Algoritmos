# https://codeforces.com/contest/263/problem/A
# Reprak11

mydata=[]

for i in range(5):
    mydata.append(list(map(int, input().strip().split())))

pos = 0
while(pos<5):
    if (sum(mydata[pos])==1):
        print(abs(pos-2)+abs(mydata[pos].index(1)-2))
        break
    pos += 1