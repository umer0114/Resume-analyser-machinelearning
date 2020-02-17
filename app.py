"""

 █████╗ ██████╗  █████╗ ███╗   ███╗ █████╗ ███╗   ██╗████████╗██╗██╗   ██╗███╗   ███╗
██╔══██╗██╔══██╗██╔══██╗████╗ ████║██╔══██╗████╗  ██║╚══██╔══╝██║██║   ██║████╗ ████║
███████║██║  ██║███████║██╔████╔██║███████║██╔██╗ ██║   ██║   ██║██║   ██║██╔████╔██║
██╔══██║██║  ██║██╔══██║██║╚██╔╝██║██╔══██║██║╚██╗██║   ██║   ██║██║   ██║██║╚██╔╝██║
██║  ██║██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║   ██║   ██║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝     ╚═╝

"""

from flask import (Flask,render_template, request)

import machine_learning
import util
import zipfile
import os
from sklearn.feature_extraction.text import CountVectorizer

from info_extractor import InfoExtractor

app = Flask(__name__)

app.config.from_object(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'docx', 'pdf'}
util.removeAllFilesFrom(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        folder = app.config['UPLOAD_FOLDER']
        f.save(os.path.join(folder, f.filename))
        # characteristics = util.getCharacteristics(folder + '/' + f.filename)

        _, classification = machine_learning.testAndClassifyResumes()
        skills = InfoExtractor.extractSkills(folder + f.filename)
        util.removeAllFilesFrom(folder)
        return render_template("single-result.html", result = {"filename": f.filename, "classification": classification[0], "skills": skills})

@app.route('/bulk-upload', methods = ['POST'])
def bulkUpload():
    if request.method == 'POST':
        f = request.files['file']
        folder = app.config['UPLOAD_FOLDER']
        with zipfile.ZipFile(f, 'r') as zip_ref:
            zip_ref.extractall(app.config['UPLOAD_FOLDER'])

        filenames, classes = machine_learning.testAndClassifyResumes()

        result = []

        for i in range(len(filenames)):
            result.append({"filename": filenames[i], "class": classes[i]})

        util.removeAllFilesFrom(folder)
        return render_template("bulk-result.html", resumesData = result)


if __name__ == '__main__':
   # app.run(debug = True)
    # app.run('127.0.0.1' , 5000 , debug=True)
    app.run('0.0.0.0' , 5000 , debug=True , threaded=True)
    
