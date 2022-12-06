# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Reprak11


if __name__ == '__main__':
    N = int(input())
    
    output_list = []
    
    for i in range (0,N):
        input_command = input().split()
        if (input_command[0] == 'insert'):
            output_list.insert(int(input_command[1]), int(input_command[2]))
        elif (input_command[0] == 'print'):
            print(output_list)
        elif (input_command[0] == 'remove'):
            output_list.remove(int(input_command[1]))
        elif (input_command[0] == 'append'):
            output_list.append(int(input_command[1]))
        elif (input_command[0] == 'sort'):
            output_list.sort()
        elif (input_command[0] == 'pop'):
            output_list.pop()
        elif (input_command[0] == 'reverse'):
            output_list.reverse()
        else:
            print('Command not available')