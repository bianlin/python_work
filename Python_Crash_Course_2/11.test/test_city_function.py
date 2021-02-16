import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
	"""测试city_function.py"""
	def test_city_country(self):
		formatted_city = get_formatted_city('santiage', 'chile')
		self.assertEqual(formatted_city, 'Santiage, Chile')

	def test_city_country_population(self):
		formatted_city = get_formatted_city(
			'santiage', 'chile', 'population=5000000')
		self.assertEqual(formatted_city, 'Santiage, Chile - Population=5000000')


if __name__ == '__main__':
	unittest.main()