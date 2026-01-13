word = input()
capital = []

for index in range(len(word)):

    if word[index].isupper():
        capital.append(index)

print(capital)