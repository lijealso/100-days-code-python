alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''
def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        idx = alphabet.index(letter)
        new_idx = idx + shift
        new_letter = alphabet[new_idx]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(text, shift):
    decipher_text = ""
    for letter in text:
        idx = alphabet.index(letter)
        new_idx = idx - shift
        new_letter = alphabet[new_idx]
        decipher_text += new_letter
    print(f"The decoded text is {decipher_text}")
'''

def caesar(dir, text, shift):
    output = ""
    for letter in text:
        idx = alphabet.index(letter)
        if dir == "encode":
            new_idx = idx + shift
        else:
            new_idx = idx - shift
        new_letter = alphabet[new_idx]
        output += new_letter
    if dir == "encode":
        print(f"The encoded text is {output}")
    else:
        print(f"The decoded text is {output}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caesar(direction, text, shift)