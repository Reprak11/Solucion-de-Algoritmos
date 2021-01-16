# http://codeforces.com/contest/218/problem/A
# Reprak11

n, k = map(int, input().strip().split())
points = list(map(int, input().strip().split()))

p=1
while(p<=(2*n+1) and k>0):
    if((p+1)%2==0):
        if points[p]-1 > points[p-1] and points[p]-1 > points[p+1]:
            points[p] -= 1
            k -= 1
    p+=1
print(' '.join(str(e) for e in points))