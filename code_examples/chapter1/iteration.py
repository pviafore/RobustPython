text = "This is some generic text"
index = 0
while index < len(text):
    print(text[index])
    index += 1


for character in text:
    print(character)

print("\n".join(text))
