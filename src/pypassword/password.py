import random


def create_password(
    available_characters: set[bytes],
    length: int,
) -> bytes:
    if not length or not available_characters:
        return b''
    list_characters = list(available_characters)
    buffer = [random.choice(list_characters) for _ in range(length)]
    return bytearray(buffer)
