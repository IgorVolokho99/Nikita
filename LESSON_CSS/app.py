from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/table')
def table():
    data = [
        {"date": "10.01.2010", "temperature": 30, "city": "Moscow"},
        {"date": "10.01.2010", "temperature": 30, "city": "SPB"},
        {"date": "10.01.2010", "temperature": 30, "city": "Rostov"},
    ]

    images = ["storm.png" if prescreiption > 0 else "sun.png" if prescreiption > 1 else "asdsa" for prescreiption in response]
    return render_template('table.html', data=data, image_name="cloud.png")


if __name__ == '__main__':
    app.run(debug=True)
