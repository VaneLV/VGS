from app import app
from flask import render_template, request, jsonify
import requests
import os


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    


@app.route('/add_message', methods=['POST'])
def add_message():
    Card = request.form['Card']
    CVV = request.form['CVV']
    Expiration = request.form['Expiration']
    response = requests.post("https://tntxb8fbmkb.SANDBOX.verygoodproxy.com/post",
                          json={'Card': Card,
                                'CVV': CVV,
                                'Expiration': Expiration})
    return render_template('message.html', Card=Card, CVV=CVV, Expiration=Expiration)
    


@app.route("/forward", methods=['POST'])
def forward():
    Card = request.form['Card']
    CVV = request.form['CVV']
    Expiration = request.form['Expiration']

    
    os.environ['HTTPS_PROXY'] = 'http://USowc3EE863TYarTKPEYXZz2:d70597f3-c00c-4d30-83fe-5324d75539e3@tntxb8fbmkb.SANDBOX.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                        json={'Card': Card,
                                'CVV': CVV,
                                'Expiration': Expiration},
                        verify='/mnt/c/Users/simple_app_test_vgs-master/simple_app_test_vgs-master/sandbox.pem')

    res = res.json()
    return render_template('forward.html', response=res)
