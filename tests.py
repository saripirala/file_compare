import unittest
from unittest import mock

import file_compare


class TestDataCompare(unittest.TestCase):
    def test_directory_read(self):
        self.assertEqual(file_compare.compare(), True)

    @mock.patch('os.walk')
    def test_read_dir_exception(self, os_walk):
        os_walk.side_effect = OSError
        with self.assertRaises(OSError):
            file_compare.compare()
