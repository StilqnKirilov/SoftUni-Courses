number = int(input())

for index in range(1, number + 1):
    digit_sum = 0
    current = index

    while current > 0:
        digit_sum += current % 10
        current //= 10

    is_special = False

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True

    print(f"{index} -> {is_special}")


