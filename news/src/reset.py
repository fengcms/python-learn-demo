#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import model

API_PREFIX = '/api/v1'
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
# parser.add_argument('article')
parser.add_argument('pagesize', type=int)
parser.add_argument('page', type=int)

class Article(Resource):
    def get(self, id):
        return {'aaa': 'get'}

    def delete(self, id):
        return {'aaa': 'del'}

    def put(self, id):
        return {'aaa': 'put'}

class ArticleList(Resource):
    def get(self):
        return model.artiListGet(parser.parse_args())

    def post(self):
        print(reqparse)
        return {'aaa': 'post'}


api.add_resource(Article, API_PREFIX + '/article/<id>')
api.add_resource(ArticleList, API_PREFIX + '/article')

if __name__ == '__main__':
    app.run(debug=True)
