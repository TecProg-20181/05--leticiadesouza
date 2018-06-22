import unittest
import subprocess
import os

from diskspace import diskspace

class BytesToReadableTest(unittest.TestCase):

    def test_bytes_values(self):
        blocks = 0
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('0.00B', bytes_size)


    def test_bytes_values(self):
        blocks = 1
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('512.00B', bytes_size)


    def test_return_type(self):
        blocks = 0
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertIsInstance(bytes_size, str)


class SubprocessCheckOutputTest(unittest.TestCase):
  # Tests relative to the subprocess_check_output method.
