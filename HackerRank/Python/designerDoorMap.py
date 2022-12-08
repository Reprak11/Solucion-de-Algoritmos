n, m = list(map(int,input().split()))
symbol = '.|.'

for i in range(1,int((n+1)/2)):
    print((symbol*(i*2-1)).center(m,'-'))

print("WELCOME".center(m,'-'))


for i in range(int((n-1)/2),0,-1):
    print((symbol*(i*2-1)).center(m,'-'))