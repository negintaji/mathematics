# https://github.com/negintaji/mathematics.git


from statistics import mean

while True:
    try:
        numbers = list(map(float, input().split()))

        if not numbers:
            raise ValueError

        print(f"{mean(numbers):.2f}")
        break

    except ValueError:
        print("Invalid Input! Enter a valid input.")

