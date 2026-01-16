key = int(input())
number_of_chars = int(input())
decryption = ""

for _ in range(number_of_chars):
    char = input()
    char_number = ord(char) + key
    decryption += chr(char_number)

print(decryption)