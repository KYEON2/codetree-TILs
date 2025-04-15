n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return a * b // gcd(a, b)

def lcm_recursive(nums, n):
    if n == 1:
        return nums[0]
    return lcm(nums[n - 1], lcm_recursive(nums, n - 1))

print(lcm_recursive(arr, n))