n = int(input())


def printS (n):
    if n <= 0:  
        return
    print("* " * n.rstrip())

    printS(n-1)
    print("* " * n.rstrip())

printS(5)