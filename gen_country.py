import random
from country import Country, countries


def create_country_list():
    """Return list of country titles from json."""

    countries_list = []
    for country in countries:
        some_country = Country(countries[country]['title'])
        countries_list.append(some_country.title)
    return countries_list


def gen_country():
    """Return random country title from the list.
    Returns:
    string: Country title.
    """
    return random.choice(create_country_list())