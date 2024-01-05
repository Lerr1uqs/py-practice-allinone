import unittest
import mock
from src import myFunction

class RandomTest(unittest.TestCase):
    # patch ('some_module.some_object') and pass it to MagicMock
    @mock.patch('os.urandom')
    def test_Random(self, random_mock: mock.MagicMock):
        random_mock.return_value = 'aaa'
        self.assertEqual(myFunction.Random(2), '2aaa')