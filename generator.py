import string
import random

def gen_pass(numbers: bool, uppercase: bool, lowercase: bool, specialcharacters: bool, length: int) -> str:
    # Define the character sets to use
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Initialize the list of character sets to use
    char_sets = []
    if numbers:
        char_sets.append(digits)
    if uppercase:
        char_sets.append(letters.upper())
    if lowercase:
        char_sets.append(letters.lower())
    if specialcharacters:
        char_sets.append(special_chars)

    # Generate the password using the selected character sets
    password = ''.join(random.choices(''.join(char_sets), k=length))
    return password
