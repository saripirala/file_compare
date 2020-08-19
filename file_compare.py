import logging
import os
from os.path import getsize, join

LOGGER = logging.getLogger(__name__)


def compare():
    try:
        for root, dirs, files in os.walk('data/from/compare'):
            LOGGER.debug(root, 'consumes', end=' ')
            LOGGER.debug(
                sum(getsize(join(root, name)) for name in files), end=' ')
            LOGGER.debug('bytes in', len(files), 'non-directory files')
    except OSError as e:
        LOGGER.error('Exception occurred while reading from/compare', e)

    try:
        for root, dirs, files in os.walk('data/to/compare'):
            LOGGER.debug(root, 'consumes', end=' ')
            LOGGER.debug(
                sum(getsize(join(root, name)) for name in files), end=' ')
            LOGGER.debug('bytes in', len(files), 'non-directory files')
    except OSError as e:
        LOGGER.error('Exception occurred while reading to/compare', e)

    return True


if __name__ == '__main__':  # pragma: no cover
    compare()
