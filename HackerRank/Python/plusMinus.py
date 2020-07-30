# https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Reprak11

def plusMinus(arr):
    cnt = [0, 0, 0]
    for i in range(len(arr)):
        if(arr[i] > 0):
            cnt[0] += 1
        elif (arr[i] < 0):
            cnt[1] += 1
        else:
            cnt[2] += 1
    for element in cnt:
        print("{:.6f}".format(element/len(arr)))  

    return 


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)