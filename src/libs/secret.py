
import string
import random

from secrets import token_bytes
from base64 import b64encode


def get_string_byte(count_bytes) -> str:
    if count_bytes:
        return b64encode(token_bytes(count_bytes)).decode()


def get_line_for_random_sample(settings: dict) -> str:

    base_line = ''
    if settings.get('letters_lowercase'):
        base_line += string.ascii_lowercase
    if settings.get('letters_uppercase'):
        base_line += string.ascii_uppercase
    if settings.get('digits'):
        base_line += string.digits
    if settings.get('punctuation'):
        base_line += string.punctuation
    return base_line


def get_result_text(settings: dict, count_symbols: int) -> str:

    result = 'not generate'

    if settings.get('bytes'):
        result = get_string_byte(count_symbols)

    else:
        line = get_line_for_random_sample(settings) * (count_symbols//5)
        result = ''.join(random.sample(line, k=count_symbols))

    return result


def get_result(settings_dict: dict, count_symbols) -> str:

    result = 'count_symbols must be integer > 0'

    try:
        count_symbols = int(count_symbols)
    except:
        count_symbols = 0

    if count_symbols > 0:
        result = get_result_text(settings_dict, count_symbols)

    return result
