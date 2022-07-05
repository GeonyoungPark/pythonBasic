from flask import Flask
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def root():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return 'No parameter'

    parameters = ''
    for key in parameter_dict.keys():
        parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
    return parameters

@app.route('/para')
def para():
    return 'PARA'

if __name__ == '__main__':
    app.run()