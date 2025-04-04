from flask import Flask, render_template, request
import random

app = Flask(__name__)


def check_domain(domain):
    return random.choice([True, False])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/domain', methods=['GET', 'POST'])
def domain():
    availability = None
    domain_name = None
    if request.method == 'POST':
        domain_name = request.form.get('domain')
        availability = check_domain(domain_name)
    return render_template('main.html', availability=availability, domain=domain_name)


if __name__ == '__main__':
    app.run(debug=True)