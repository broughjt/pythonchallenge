import string


caption = string.ascii_lowercase 
new_string = ""

for letter in caption:
    found_position = string.ascii_lowercase.find(letter)

    if found_position == -1:
        new_string += letter
        continue
    
    index = found_position + 2

    if index >= 26:
        index -= 26

    new_string += string.ascii_lowercase[index]

table = string.maketrans(string.ascii_lowercase, new_string)
NEW_STRING = string.translate("map", table)
print(NEW_STRING)

