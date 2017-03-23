import unittest

import module

class TestGenerateData(unittest.TestCase):
    def test_generate_data(self):
        data = module.generate_data()
        self.assertEqual(data.shape, (10, 10))
