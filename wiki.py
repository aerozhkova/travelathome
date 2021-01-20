import wikipediaapi
import wikipedia


wiki_html = wikipediaapi.Wikipedia(
        language='ru',
        extract_format=wikipediaapi.ExtractFormat.HTML
)
wikipedia.set_lang("ru")

def get_summary(object):
        """Return summary of the object page.
        Args:
        object ('string'): title of wiki-object.
        Returns:
        string: summary in html-format.
        """
        try:
                wipage = wiki_html.page(object)
        except(Exception):
                pass
        else:
                return wipage.summary

def get_title(object):
        """Return title of the object page.
        Args:
        object ('string'): title(path) of wiki-object.
        Returns:
        string: nice title of wiki-object.
        """
        object_str = object.replace('_', ' ')
        try:
                wipage = wikipedia.page(object_str)
        except(Exception):
                return 'Название не найдено'
        else:
                return wipage.title