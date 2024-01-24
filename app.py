from flask import Flask, render_template, request
import short_url
from short_url import create_short_url, retrive_from_dynamo

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')
    return 'Hi everyone'

# post parameter from url
@app.route('/short_url', methods=['POST'])
def short_url_post():
    data = request.get_json()
    url = data.get('url')
    # url = request.form['url'] // this working if you use form from postman
    return create_short_url(url)

#get full url from short url
@app.route('/get_full_url', methods=['GET'])
def redirect_short_url():
    short_url = request.args.get('short_url', default=None, type=str)
    full_url = retrive_from_dynamo(short_url)
    return full_url['url']

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)

