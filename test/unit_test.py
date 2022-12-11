import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from src.main import printingInitialMessage


class TestUnittestFramework(unittest.TestCase):
    def test_main(self):
        self.assertEqual(printingInitialMessage(), "Initial message.")


if __name__ == '__main__':
    unittest.main()
