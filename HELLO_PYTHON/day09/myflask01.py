import json

from flask import Flask
from flask.globals import request
from flask.json import jsonify
from flask.templating import render_template

from day09 import daoemp
from day09.daoemp import DaoEmp


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'


@app.route('/para')
def get():
    a = request.args.get('a')
    return "para " + a

@app.route('/post',methods=['post','get'])
def post():
    value = request.form['a']
    return 'POST' + value

@app.route('/dyna')
def dyna():
    a = "홍길동"
    b = ["홍길동","전우치","이순신"]
    c = [
        {"e_id" : "1","e_name" : "2","sex" : "3","addr" : "4"},
        {"e_id" : "5","e_name" : "6","sex" : "7","addr" : "8"}
    ]
    return render_template("dyna.html", a = a, b = b, c = c)

@app.route('/emp_list')
def emp_list():
    de = DaoEmp()
    e = de.selects()
    return render_template("emp_list.html",e=e)

if __name__ == '__main__':
    app.run()