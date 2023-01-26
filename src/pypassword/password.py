import random


def create_password(
    available_characters: set[bytes],
    length: int,
) -> bytes:
    """Gets `length` random bytes from `available_characters` and create a new bytes sequence from it
    """
    if length < 0:
        raise RuntimeError(f'Length must be positive not {length}')
    if not available_characters:
        return b''
    list_characters = list(available_characters)
    buffer = [random.choice(list_characters) for _ in range(length)]
    return bytearray(buffer)
