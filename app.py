from flask import Flask, render_template, request
import multiple_metrixes
import metrix_multiplication

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')
    return 'Hi everyone'

@app.route('/multiple')
def multiple():
    # return render_template('index.html')
    return multiple_metrixes.multiple(5,4)

@app.route('/multiple_m')
def multiple_m():
    # return render_template('index.html')
    return metrix_multiplication.multiple_matrixes()

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return render_template('greet.html', name=name)


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)

