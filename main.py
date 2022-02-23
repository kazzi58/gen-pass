import string
import random

def generate_password(length_of_password, contain_all_types):
    password = []

    # get all the English lowercase characters
    # abcdefghijklmnopqrstuvwxyz
    lowercase_letters = string.ascii_lowercase

    # get all the English uppercase characters
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    uppercase_letters = string.ascii_uppercase

    # get all the digits
    # 0123456789
    digits = string.digits

    # get all the special characters
    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    special_characters = string.punctuation

    # combining all the characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    if contain_all_types:
    # forcing the password to contain at least one character from each type
    # taking one character from each type
        random_lowercase_letter = random.sample(lowercase_letters, 1)
        random_uppercase_letter = random.sample(uppercase_letters, 1)
        random_digit = random.sample(digits, 1)
        random_special_character = random.sample(special_characters, 1)

        if length_of_password < len(all_characters):
            # randomly sampling n-4 characters from the list of all possible characters
            password = random.sample(all_characters, length_of_password - 4)

            # combining the previous 4 characters (one from each type) with the randomly sampled characters
            full_password = password + \
                            random_lowercase_letter + \
                            random_uppercase_letter + \
                            random_special_character + \
                            random_digit

            # shuffling the whole list to ensure there isn't any fixed pattern
            random.shuffle(full_password)
            return full_password

        else:
            for _ in range(length_of_password - 4):
                random_character = random.sample(all_characters, 1)
                password = password + random_character
            full_password = password + \
                            random_lowercase_letter + \
                            random_uppercase_letter + \
                            random_special_character + \
                            random_digit
            random.shuffle(full_password)
            return full_password
    else:
    # contain_all_types parameter = 0
    # there is no need to ensure that every type of character is in the password
        if length_of_password < len(all_characters):
            password = random.sample(all_characters, length_of_password)
            return password
        else:
            for _ in range(length_of_password):
                random_character = random.sample(all_characters, 1)
                password = password + random_character
            return password


# define this variable as per the requirement
length_of_password = 80

generated_password = "".join(generate_password(length_of_password, 1))
print(generated_password)

