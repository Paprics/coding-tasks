import unittest
from ..utils import formatted_name


class TestFormattedName(unittest.TestCase):

    fn = 'first_name'
    ln = 'last_name'
    mn = 'middle_name'

    def test_formatted_name_valid(self):
        self.assertEqual(formatted_name(self.fn, self.ln), f'{self.fn.title()} {self.ln.title()}')

    def test_formatted_name_invalid_full_name(self):
        self.assertEqual(formatted_name(self.fn, self.ln, self.mn),
                         f'{self.fn.title()} {self.mn.title()} {self.ln.title()}')

    def test_formatted_name_empty(self):
        self.assertEqual(formatted_name('', ''), ' ')



if __name__ == '__main__':
    unittest.main()