import pytest
import logging

import src.pypassword.utils as utils

@pytest.mark.parametrize(
    'level,root',
    (
        (logging.NOTSET, True),
        (logging.DEBUG, True),
        (logging.INFO, True),
        (logging.WARNING, False),
        (logging.ERROR, False),
        (logging.CRITICAL, False)
    ),
)
def test_logging_setup(level, root):
    utils.setup_logger(level=level, root=root)

    # Get utils library logger
    if root:
        logger = logging.getLogger()
        assert logger.parent is None
    else:
        logger = logging.getLogger(utils.__name__)
        assert logger.parent is not None

    # Assert setup_logger correctly configured it
    assert logger.getEffectiveLevel() == level
