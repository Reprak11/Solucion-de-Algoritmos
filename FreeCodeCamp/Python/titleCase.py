def titleCase(str):
    str = str.split()
    for i in range(len(str)):
        str[i] = str[i].capitalize()
    return ' '.join(str)

if __name__ == "__main__":
    print(titleCase(input()))