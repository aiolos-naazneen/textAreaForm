from urllib.request import urlopen
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


def makeAPICall():
    import json
    # url = "https://jsonplaceholder.typicode.com/todos/5"
    # with urlopen(url) as response:
    #     body = response.read()
    # todo_item = json.loads(body)
    json_body = {
        'title': "Buy Donuts",
        'completed': False,
        'userId': 1,
        'targetDate': '2020-01-01',
        'status': 'active'
    }
    return json_body


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        query = request.form['query']
        print("query:", query)
        response = makeAPICall()
        return render_template("form.html", result=response)
    else:
        user = request.args.get('nm')
        return render_template("form.html")


if __name__ == '__main__':
    app.run(debug=True)
