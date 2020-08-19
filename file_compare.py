import os
from os.path import join, getsize


class CyclicDependencyError(ValueError):
    """Raised whe a circular dependency is found"""


def compare():
    try:
        for root, dirs, files in os.walk('data/from/compare'):
            print(root, "consumes", end=" ")
            print(sum(getsize(join(root, name)) for name in files), end=" ")
            print("bytes in", len(files), "non-directory files")
    except OSError as e:
        print('Exception occurred while reading from/compare', e)

    try:
        for root, dirs, files in os.walk('data/to/compare'):
            print(root, "consumes", end=" ")
            print(sum(getsize(join(root, name)) for name in files), end=" ")
            print("bytes in", len(files), "non-directory files")
    except OSError as e:
        print('Exception occurred while reading to/compare', e)

    return True


if __name__ == "__main__":
    compare()
