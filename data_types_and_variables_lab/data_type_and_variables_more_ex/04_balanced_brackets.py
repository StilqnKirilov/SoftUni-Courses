number_of_lines = int(input())

open_bracket = False
balanced = True

for _ in range(number_of_lines):
    line = input()

    if line == "(":
        if open_bracket:
            balanced = False
            break
        open_bracket = True

    elif line == ")":
        if not open_bracket:
            balanced = False
            break
        open_bracket = False

if open_bracket :
    balanced = False

if balanced:
    print("BALANCED")

else:
    print("UNBALANCED")