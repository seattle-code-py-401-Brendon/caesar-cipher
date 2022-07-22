from clock_queue import Clock_queue
import string

"""
save a list of the alphabet
create a function called encrypt
      takes in two parameters
        phrase(string), num(shift)
the phrase will then be shifted that many letters of the alphabet
shifts that exceed 26 should wrap around.
shifts that push a letter out or range should wrap around.
"""

"""
Create a function called decrypt
    takes in the encrypted message and performs the encrypt but with the negative shift
Create a crack method that brute forces through all the shifts 
"""


# create alphabet

# create encrypt function
def encrypt(phrase=None, shift=None):
    alphabet = Clock_queue()
    secret_message = ''
    # the encryption clock

    lower_alphabets = list(string.ascii_lowercase)

    for letter in lower_alphabets:
        alphabet.enqueue(letter, 'r')

    for unchanged_letter in phrase:
        if unchanged_letter.isupper():
            encrypted_letter = alphabet.clock_wise(unchanged_letter.lower(), shift)
            secret_message += encrypted_letter.upper()
        else:
            encrypted_letter = alphabet.clock_wise(unchanged_letter, shift)
            secret_message += encrypted_letter

    return secret_message


def decrypt(phrase=None, shift=None):
    alphabet = Clock_queue()
    decrypt_msg = ''
    lower_alphabets = list(string.ascii_lowercase)

    for letter in lower_alphabets:
        alphabet.enqueue(letter, 'r')

    for changed_letter in phrase:
        if changed_letter.isupper():
            d = alphabet.counter_clock_wise(changed_letter.lower(), shift)
            decrypt_msg += d.upper()
        else:
            d = alphabet.counter_clock_wise(changed_letter, shift)
            decrypt_msg += d

    return decrypt_msg


def crack():
    pass


if __name__ == "__main__":
    list1 = encrypt("Gimme a 1!", 1)
    print(list1)
    print(decrypt(list1, 1))
