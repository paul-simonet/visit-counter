import os

import redis
from flask import Flask, jsonify

app = Flask(__name__)
db = redis.Redis(host=os.environ["DB_HOST"])

@app.get("/visits")
def visits():
    reply = jsonify(visits=db.incr("visits"))
    reply.headers["Access-Control-Allow-Origin"] = "http://localhost:8081"
    return reply
