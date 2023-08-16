string = input("Please enter a string: ")

char_count = {}

for char in string:
    if char.isalpha():
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

sorted_chars = sorted(char_count.keys(), key=lambda char: char_count[char], reverse=True)

for char in sorted_chars:
    print(f"{char} = {char_count[char]:02d}")
