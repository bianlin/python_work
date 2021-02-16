def get_formatted_city(city, country, population=''):
	"""返回整洁的城市，国家"""
	if population:
		formatted_city = f"{city}, {country} - {population}"
	else:
		formatted_city = f"{city}, {country}"
	return formatted_city.title()
