# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Reprak11

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = (sorted(set(arr)))[-2]
    
    print(arr)