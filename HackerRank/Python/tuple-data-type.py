# https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Reprak11

if __name__ == '__main__':
    
    n = int(input())
    value = map(int,input().split())
    t = tuple(value)
    
    print(hash(t))