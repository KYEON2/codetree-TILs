n = int(input())


def printS (n):
    if n <= 0:  
        return
    print("* "*n)

    printS(n-1)
    print("* "*n)

printS(5)