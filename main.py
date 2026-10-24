# https://github.com/negintaji/mathematics.git

from statistics import mean

numbers = list(map(float, input().split()))

print(f"{mean(numbers):.2f}")
