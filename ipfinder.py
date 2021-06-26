from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        if not request.form['name'] or not request.form['age']:
            return render_template('index.html')
        else:
            return redirect('/myip/{}/{}'.format(request.form['name'], request.form['age']))


@app.route('/myip/<name>/<age>')
def myip(name, age):
    myip = requests.get('http://api.ipify.org/').text
    username = f'{name}{age}'
    return render_template('myip.html', n=username, ip=myip)

if __name__ == '__main__':
    app.run(debug=True)