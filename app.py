from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from PIL import Image
import base64
from io import BytesIO
import base64
import os
import time
import json
app = Flask(__name__, static_url_path='/', static_folder='./')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

        
@app.route('/Get', methods=['GET'])
@cross_origin()
def get():
    filename = request.args.get('filename', '')
    path = os.path.join('./files/',filename)
    if os.path.exists(path):
        return send_file(path,as_attachment=True, attachment_filename=filename)


if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 8888, ssl_context='adhoc')