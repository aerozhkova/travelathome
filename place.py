from get_image import get_img_url
from wiki import get_summary, get_title


class Place():
    def __init__(self, title):
        """Constructor of Place.

        Accepts parameter title.
        Initializes a Place with title.
        """
        self.title = title

    @property
    def wiki_title(self):
        """Returns wiki-format title of the Place."""
        return get_title(self.title)

    @property
    def summary(self):
        """Returns wiki-summary of the Place in html format."""
        return get_summary(self.title)

    @property
    def image_url(self):
        """Returns first image in wiki-infobox of the Place."""
        return get_img_url(self.title)
