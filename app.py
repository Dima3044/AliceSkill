from flask import Flask, request
app = Flask(__name__)
import logging

@app.route('/', methods = ['POST'])
def main():
  logging.info(request.json)
