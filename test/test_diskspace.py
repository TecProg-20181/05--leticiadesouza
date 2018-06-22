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


    def test_tbytes(self):
        blocks = 10000000000
        bytes_size = diskspace.bytes_to_readable(blocks)
        label = bytes_size[-2:]
        self.assertEqual('Tb', label)


    def test_gbytes(self):
        blocks = 10000000
        bytes_size = diskspace.bytes_to_readable(blocks)
        label = bytes_size[-2:]
        self.assertEqual('Gb', label)


    def test_mbytes(self):
        blocks = 100000
        bytes_size = diskspace.bytes_to_readable(blocks)
        label = bytes_size[-2:]
        self.assertEqual('Mb', label)

    def test_kbytes(self):
        blocks = 1000
        bytes_size = diskspace.bytes_to_readable(blocks)
        label = bytes_size[-2:]
        self.assertEqual('Kb', label)
