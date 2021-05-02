# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask import render_template
import os
from app import camera

UPLOAD_FOLDER = 'thumbnail_images'
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'mp4', 'bmp'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.after_request
def add_header(r):
   """
   Add headers to both force latest IE rendering engine or Chrome Frame,
   and also to cache the rendered page for 10 minutes.
   """
   r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
   r.headers["Pragma"] = "no-cache"
   r.headers["Expires"] = "0"
   r.headers['Cache-Control'] = 'public, max-age=0'
   return r


@app.route('/', methods=['GET'])
def static_page():
    return render_template("newpage.html")


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    upload_to = 'static/videos/'
    output = {}
    file_upload = request.files['file']
    print('File Name>>>>>>>', file_upload.filename)
    file_upload.save(os.path.join(upload_to, 'temp.mp4'))
    camera.start_app('static/videos/temp.mp4')
    return render_template('output.html', output_list=output)


@app.route('/output.html', methods=['GET', 'POST'])
def open_detection():
    return render_template('output.html')


# ---------------------------- Request For Demo ------------------------------------#


if __name__ == '__main__':
    app.run(debug=True, port=5011)
