import random
import string

length = input("Length of your password")
length = int(length)

# print(randnum)

def gen_func():
    letters = string.ascii_letters
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_charac = string.punctuation
    randnum = ''.join(random.choices(letters+lower_case+upper_case+digits+special_charac,k=length))

def gen_pass(numbers:bool, uppercase:bool, lowercase:bool, specialcharacters:bool, length:int) ->string:
    

password = gen_pass(False, length)
print(password)
