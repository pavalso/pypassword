import pytest
import string

import src.pypassword.password as password


def test_create_password_boundaries():
    with pytest.raises(RuntimeError):
        password.create_password(set(b'Some Bytes'), -1)
    assert password.create_password(set(b'Some Bytes'), 0) is b''

@pytest.mark.parametrize(
    'byte_seq,length',
    (
        (set(b'abcdefghijklmnopqrstuvwxyz'), 12),
        (set(b'123456789'), 8),
        (set(b'abcdefghijklmnopqrstuvwxyz123456789'), 16),
        (set(string.printable.encode()), 64)
    )
)
def test_random_password_creation(byte_seq, length):
    for _ in range(1000):
        out = password.create_password(byte_seq, length)

        # Check generated password is valid
        assert len(out) == length
        assert all([byte in byte_seq for byte in out])
