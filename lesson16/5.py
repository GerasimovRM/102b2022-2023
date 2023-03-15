alphabet = "".join(sorted('йцукенгшщзхъфывапролджэячсмитьбю'))
# alphabet = ''.join([chr(i) for i in range(ord('а'), ord('я') + 1)])


def from_letter_to_encrypt(letter, shift):
    if letter.lower() in alphabet:
        pos = alphabet.find(letter.lower())
        new_letter = alphabet[(pos + shift) % len(alphabet)]
        if letter.isupper():
            new_letter = new_letter.upper()
        return new_letter
    else:
        return letter


def encrypt_caesar(text, shift):
    return "".join([from_letter_to_encrypt(sym, shift)
                    for sym in text])


def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)


msg = "Да здравству}{}#&@^%$&@#^%$ет салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)