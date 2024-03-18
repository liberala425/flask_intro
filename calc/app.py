# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_func():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(add(a,b))

@app.route('/sub')
def sub_func():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(sub(a,b))

@app.route('/mult')
def mult_func():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(mult(a,b))

@app.route('/div')
def div_func():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(div(a,b))

@app.route('/math/<operation>')
def math_func(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    oper_dic = {"add": add, "sub": sub, "mult": mult, "div": div}
    return str(oper_dic[operation](a,b))
    """
    if operation == "add":
        return str(add(a,b))
    elif operation == "sub":
        return str(sub(a,b))
    elif operation == "mult":
        return str(mult(a,b))
    elif operation == "div":
        return str(div(a,b))
    """