from wiki import get_summary
import json

with open('countries.json', 'r', encoding='utf-8') as f:
    countries = json.load(f)


class Country():
    def __init__(self, title):
        """Constructor of Country.
        Accepts parameter title.
        Initializes a Country with title.
        """
        self.title = title

    @property
    def code(self):
        return countries[self.title]['code']

    @property
    def map(self):
        return countries[self.title]['map']

    @property
    def summary(self):
        """Returns wiki-summary of the Place in html format."""
        return get_summary(self.title)

    @property
    def flag(self):
        """Returns html-tag of the Country flag."""
        img_tag = "<img alt=Тут&nbsp;должен&nbsp;быть&nbsp;флаг&nbsp;страны,&nbsp;но&nbsp;его&nbsp;нет&nbsp;:( src=https://www.countryflags.io/" + \
                  self.code + "/flat/64.png>"
        return img_tag