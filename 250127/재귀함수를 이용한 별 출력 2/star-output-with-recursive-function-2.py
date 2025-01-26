n = int(input())


def printS(n):
    if n <= 0:  
        return
    print(" ".join(["*"] * n))  # 줄 끝 공백 제거

    printS(n - 1)
    print(" ".join(["*"] * n))  # 줄 끝 공백 제거


printS(n)
