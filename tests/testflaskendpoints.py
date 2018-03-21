import json

from flask import Flask
from flask_testing import TestCase
from manage import app


class TestFlaskEndpoints(TestCase):
    def create_app(self) -> Flask:
        return app

    def test_float_sum_request(self):
        response = self.client.get('/float_sum?val1=1.1&val2=2.0')

        self.assert200(response)

    def test_sum_columns_request(self):
        response = self.client.post('/sum_columns', data=json.dumps({'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]}),
                                    content_type='application/json')

        self.assert200(response)
