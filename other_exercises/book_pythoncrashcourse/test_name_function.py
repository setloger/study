import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""

    def test_first_last_name(self):
        """Имена вида 'Oleg Ivanov' работают правильно?"""
        formatted_name = get_formatted_name('oleg', 'ivanov')
        self.assertEqual(formatted_name, 'Oleg Ivanov')

    def test_first_last_middle_name(self):
        """Работают ли такие имена, как 'Andrey Nikolaevich Ivanov'"""
        formatted_name = get_formatted_name('Andrey', 'Ivanov', 'Nikolaevich')
        self.assertEqual(formatted_name, 'Andrey Nikolaevich Ivanov')

unittest.main()