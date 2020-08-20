import logging
import os
from os.path import getsize, join

LOGGER = logging.getLogger(__name__)


def read_dir(path):
    try:
        for root, dirs, files in os.walk('data/from/compare'):
            LOGGER.debug(root, 'consumes', end=' ')
            LOGGER.debug(
                sum(getsize(join(root, name)) for name in files), end=' ')
            LOGGER.debug('bytes in', len(files), 'non-directory files')
        return files
    except OSError as e:
        LOGGER.error(
            'Exception occurred while reading %s %s', path, str(e))
        raise OSError


def compare():
    from_compare = read_dir('data/from/compare')
    to_compare = read_dir('data/to/compare')
    LOGGER.debug('list of files %s', from_compare)
    LOGGER.debug('list of files %s', to_compare)
    return True


if __name__ == '__main__':  # pragma: no cover
    compare()
