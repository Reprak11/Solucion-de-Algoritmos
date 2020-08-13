def trucateString(str, num):
    palabra = ""
    for i in range(num):
        palabra += str[i]
    palabra += " ..."
    return palabra

if __name__ == "__main__":
    print(trucateString("Peter Piper picked a peck of pickled peppers", 11))