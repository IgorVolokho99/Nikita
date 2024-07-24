from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    redirect_url = url_for('result', name=name, email=email)
    return jsonify({'redirect_url': redirect_url})

@app.route('/result')
def result():
    name = request.args.get('name')
    email = request.args.get('email')
    return render_template('result.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
