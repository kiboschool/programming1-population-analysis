from flask import Flask, render_template
import main

app = Flask(__name__)


@app.route('/')
def index():
    list_sz = main.read_json(item_to_read='list_size')
    countries_dict = main.pop_density()
    mod_dict = dict(list(countries_dict.items())[0: list_sz])
    return render_template('index.html', countries=mod_dict)
