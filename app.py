import requests as requests
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
app = Flask(__name__)

from pymongo import MongoClient
# 꼭 디비 주소 없애기ㅠㅠㅠ

db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.fanBoard.insert_one(doc)

    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    comment_list = list(db.fanBoard.find({}, {'_id': False}))
    return jsonify({'comments':comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)