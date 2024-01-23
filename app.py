from flask import Flask, render_template, request
import short_url
from short_url import create_short_url

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')
    return 'Hi everyone'

# get parameter from url
@app.route('/short_url/<url>')
def short_url(url):
    # return render_template('index.html')
    return create_short_url(url)

# post parameter from url
@app.route('/short_url', methods=['POST'])
def short_url_post():
    url = request.form['url']
    return create_short_url(url)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)

