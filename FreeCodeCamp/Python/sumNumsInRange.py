# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/sum-all-numbers-in-a-range
# Reprak11
def sumAll(arr):
    if arr[0] < arr[1]:
        x = list(range(arr[0],arr[1]+1))
    else:
        x = list(reversed(range(arr[1],arr[0]+1)))
    return sum(x)

if __name__ == "__main__":
    nums = input()[1:-1]
    nums = list(map(int,nums.split(",")))
    print(sumAll(nums))
