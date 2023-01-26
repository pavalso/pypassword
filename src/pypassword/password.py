import random


def create_password(
    available_characters: set[bytes] | bytes,
    length: int,
) -> bytes:
    """
    Generates a random password of specified length using the provided set of available characters.
    
    Parameters:
        available_characters (set[bytes] | bytes): A set of characters that can be used to generate the password.
        length (int): The desired length of the generated password.
        
    Returns:
        bytes: The generated password.
        
    Raises:
        RuntimeError: If the provided length is less than 0.
    """
    if length < 0:
        raise RuntimeError(f'Length must be positive not {length}')
    if not available_characters:
        return b''
    list_characters = list(available_characters)
    buffer = [random.choice(list_characters) for _ in range(length)]
    return bytes(bytearray(buffer))
