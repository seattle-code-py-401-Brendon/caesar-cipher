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
    phrase_queue = Clock_queue()
    phrase = 'hello'

    # the phrase queue to be encrypted
    for phrase_letter in phrase:
        phrase_queue.enqueue(phrase_letter, 'r')

    phrase_queue.clock_wise()
    phrase_queue.print()

    # the encryption clock
    lowercase_alphabets = list(string.ascii_lowercase)
    for letter in lowercase_alphabets:
        alphabet.enqueue(letter, 'r')




def decrypt():
    pass


def crack():
    pass


if __name__ == "__main__":
    encrypt()
