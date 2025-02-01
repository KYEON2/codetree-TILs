a, b, c = map(int, input().split())


def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

def process_numbers(a, b, c):
    product = a * b * c
    return sum_of_digits(product)



result = process_numbers(a, b, c)
print(result)