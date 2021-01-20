import requests
import wptools
import hashlib


def get_wikibase(object):
    """Return wikibase of a wiki-object.
    Args:
    object ('string'): title of wiki-object.
    Returns:
    string: Wikibase.
    """
    page = wptools.page(object, lang='ru')
    page_parsed = page.get_parse()
    wikibase = page_parsed.data['wikibase']
    return wikibase

def get_url(wikibase):
    """Return image url from the infobox of the wiki page.
    Args:
    wikibase ('string'): wikibase of the object, which image we want to get.
    Returns:
    string: Url of the image.
    """
    URL = "https://www.wikidata.org/w/api.php"
    PARAMS = {
    'action': 'wbgetclaims',
    'property': 'P18',
    'entity': wikibase,
    'format': 'json'
    }

    r = requests.get(url=URL, params=PARAMS)
    r_json = r.json()
    image_title = r_json['claims']['P18'][0]['mainsnak']['datavalue']['value']
    image_title = image_title.replace(' ', '_')
    my_string = image_title.encode('utf-8')
    hash_object = hashlib.md5(my_string)
    image_url = 'https://upload.wikimedia.org/wikipedia/commons/' + \
                hash_object.hexdigest()[:1] + '/' + hash_object.hexdigest()[:2] + '/' + image_title
    return image_url


def get_img_url(object):
    """Takes object and returns image url from the infobox of the wiki page.
    Args:
    object ('string'): title of wiki-object.
    Returns:
    string: Url of the image.
    """
    wikibase = get_wikibase(object)
    image_url = get_url(wikibase)
    return image_url

