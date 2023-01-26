import random


def create_password(
    available_characters: set[bytes],
    length: int,
) -> bytes:
    """Gets `length` random bytes from `available_characters` and create a new bytes sequence from it
    """
    if not length or not available_characters:
        return b''
    list_characters = list(available_characters)
    buffer = [random.choice(list_characters) for _ in range(length)]
    return bytearray(buffer)
