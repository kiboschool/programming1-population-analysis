from flask import Flask, render_template
import main, pop_analysis

app = Flask(__name__)


@app.route('/')
def index():
    pop_analysis.read_json()
    pop_analysis.create_densities()
    pop_analysis.customized_dataset()
    return render_template('index.html', countries=pop_analysis.pop_density)
