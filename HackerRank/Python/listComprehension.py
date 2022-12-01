# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
# Reprak11

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    output = [[X, Y ,Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X+Y+Z != n]
    print(output)