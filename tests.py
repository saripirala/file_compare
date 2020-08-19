import unittest

import file_compare


class TestDataCompare(unittest.TestCase):
    def test_directory_read(self):
        self.assertEqual(file_compare.compare(), True)
