# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
# Reprak11

def swap_case_2(s):
    return s.swapcase()
    
    
def swap_case(string):
    temp = ""
    for character in string:
        if character.isupper() == True:
            temp += character.lower()
        else:
            temp += character.upper()
    return temp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)