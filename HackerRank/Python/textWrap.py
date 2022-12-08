# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
# Reprak11

import textwrap

def wrap(string, max_width):
    output_string = ""
    count = int(len(string)/int(max_width))
    for i in range(int(len(string)/int(max_width))):
        output_string += str(string[i*max_width:i*max_width+max_width]) + '\n'
    output_string += string[count*max_width:] if count*max_width < len(string) else ""
    return output_string

def wrap2(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    output_string = wrapper.wrap(text=string)
    return "\n".join(output_string)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)