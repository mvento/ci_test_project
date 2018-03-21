import json

import pandas as pd
from flask import Flask, request

import random_operations

app = Flask(__name__)


@app.route('/float_sum', methods=['GET'])
def float_sum():
    value_1 = float(request.args.get('val1'))
    value_2 = float(request.args.get('val2'))

    result = {'result': random_operations.float_sum(value_1, value_2)}
    return json.dumps(result)


@app.route('/sum_columns', methods=['POST'])
def sum_columns():
    json_data = request.get_json()

    data = pd.DataFrame(json_data)

    result = {'result': random_operations.sum_columns(data).to_json()}
    return json.dumps(result)


if __name__ == '__main__':
    app.run()
