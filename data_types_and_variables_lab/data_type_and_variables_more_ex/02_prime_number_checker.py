number = int(input())
is_prime = True

if number == 0 or number == 1:
    is_prime = False

elif number > 1:
    for index in range(2, number):
        if number % index == 0:
            is_prime = False
            break

print(is_prime)
