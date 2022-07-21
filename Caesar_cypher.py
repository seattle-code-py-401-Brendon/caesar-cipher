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
alphabet = list(string.ascii_lowercase)
for i in range(len(alphabet)):
    print(i, alphabet[i])


# create encrypt function
def encrypt(phrase, shift=None):
    shifted_phrase = ''
    # get the index location for alphabet
    for letter in phrase:
        for i in range(len(alphabet) -1):
            if alphabet[i] == letter:
                letter = alphabet[i + shift]
                shifted_phrase += letter
    print(shifted_phrase)


if __name__ == "__main__":
    phrase_one = 'axbycgcdkd'
    encrypt(phrase_one, 1)
