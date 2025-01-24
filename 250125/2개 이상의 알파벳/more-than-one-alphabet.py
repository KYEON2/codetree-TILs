from collections import Counter

A = input()

alp_count = Counter(A)

if len(alp_count) > 1 :
    print("Yes")
else :
    print("No")

