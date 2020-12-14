from app import app
from flask import render_template, request, redirect, abort, jsonify
from os.path import join
from serializer import Serializer
from logger import log


TEMP_FOLDER_PATH = 'public/temp'

# Encrypt/Decrypt file based on action inpute
def serialize_file(filename, action):
    target_path = None
    if action == 'encrypt':
        target_path = Serializer.encrypt(filename)
    elif action == 'decrypt':
        target_path = Serializer.decrypt(filename)
    return target_path

# Serve the home page
@app.route('/')
def index():
    return render_template('index.html')

# Upload file to the server
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file and file.filename != '':
        log(request)
        filename = file.filename
        action = request.form.get('action')
        file.save(join(TEMP_FOLDER_PATH, filename))
        target_path = serialize_file(filename, action)
        return redirect(f'/{target_path}')
    else:
        return abort(400)


# Error handlers
@app.errorhandler(400)
def bad_request(err):
    return jsonify({
        'success': False,
        'error': 400,
        'msg': 'bad request'
    }), 400

