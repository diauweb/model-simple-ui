import os
from datetime import datetime
from flask import *  
from werkzeug.utils import secure_filename
import model

app = Flask(__name__, static_url_path='')  

@app.route('/')
def root():    
    return send_file('static/index.html')

@app.route('/upload', methods=['POST'])
def upload():
    print(request.files)
    if 'file' not in request.files:
        return jsonify({ "error": "bad form is provided "}), 400
        
    file = request.files['file']
    if file.filename == '' or ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() != 'jpg'):
        return jsonify({ "error": "no file is provided "}), 400
    
    filename = f'{datetime.now().timestamp()}.jpg'
    file.save(f'run/{filename}')
    return jsonify({ "file_handle": filename })

@app.route('/check', methods=['GET'])
def check():
    filename = request.args['handle']
    fpath = f'run/{secure_filename(filename)}'
    if not os.path.isfile(fpath):
        return jsonify({ "error": "the specified task does not exists"}), 400

    result = model.run_model(fpath)
    os.remove(fpath)
    return jsonify(result)
    
if __name__ == '__main__':  
    app.run(debug=True)
