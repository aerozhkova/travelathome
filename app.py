from flask import Flask, render_template, request

from gen_country import gen_country, create_country_list
from country import Country
from place import Place

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', country_title = gen_country())

@app.route('/usage')
def usage():
    return render_template('usage.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/<country>')
def go_to_country(country):
    country_list = create_country_list()
    if country in country_list:
        some_country = Country(country)
        return render_template('country.html', country_title = some_country.title,
                               page_summary = some_country.summary,
                               flag = some_country.flag,
                               map = render_template('country_map.html', map_link = some_country.map))
    return render_template('not_found.html')

@app.route('/places')
def api():
    if request.args.get('country') and request.args.get('place'):
        some_country = Country(request.args.get('country'))
        some_place = Place(request.args.get('place'))
        return render_template('place.html', place_title = some_place.wiki_title,
                               page_summary = some_place.summary,
                               map = render_template('country_map.html', map_link=some_country.map),
                               image_url = some_place.image_url)
    return render_template('not_found.html')

@app.errorhandler(Exception)
def all_exception_handler(error):
   return render_template('error_tech.html')

if __name__ == '__main__':
   app.run(debug = True)