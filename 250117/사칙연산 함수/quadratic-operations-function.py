a, o, c = input().split()
a = int(a)
c = int(c)

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x // y

if o == "+":
    result = plus(a, c)
    print(f"{a} + {c} = {result}")
elif o == "-":
    result = minus(a, c)
    print(f"{a} - {c} = {result}")
elif o == "/":
    result = div(a, c)
    if result == "Error":
        print(result)
    else:
        print(f"{a} / {c} = {result}")
elif o == "*":
    result = mul(a, c)
    print(f"{a} * {c} = {result}")
else:
    print("False")