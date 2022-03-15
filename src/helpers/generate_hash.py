from random import choice
import string


def generate_hash(salt=None):
    letters = string.ascii_letters
    return (''.join(choice(letters) for i in range(salt or 10)))
