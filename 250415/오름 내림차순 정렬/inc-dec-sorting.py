n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

print(*sorted(nums))

nums.sort()
arr = list(reversed(nums))
print(*arr)
