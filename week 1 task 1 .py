def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    positions = []
    for letter in text.lower():
        if letter in alphabet:
            positions.append(str(alphabet.index(letter) + 1))
    return ' '.join(positions)


text = input("Enter a string: ")
print(str(alphabet_position(text)))
