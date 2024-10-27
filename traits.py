import random

MAX_MESSAGE_LENGTH = 4096


class Generator:
    @staticmethod
    def generate_random_int(length=8):
        range_start = 10**(length-1)
        range_end = (10**length) - 1
        return random.randint(range_start, range_end)