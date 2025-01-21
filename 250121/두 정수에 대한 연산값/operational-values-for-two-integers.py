a, b = map(int, input().split())

# Write your code here!

def cal(x, y):
    if x > y:
        x += 25
        y *= 2
    elif y > x:
        y += 25
        x *= 2
    return x, y

result = cal(a, b)
print(result[0], result[1]) 
