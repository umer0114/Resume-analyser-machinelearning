# Resume Scanner
A web app to help employers to classify resumes.

## Description
A semantic analysis and classification of resumes based on roles and experience needs of an organization. We will be applying NLP techniques to read different formats, and Machine Learning Algorithms to classify the concerned resumes accordingly.

For single file scan or bulk upload, it distributes resumes' in `result/resumes/` folders as per class.

## Prerequisites

### Software
* Flask==1.1.1
* sklearn==0.0
* PyPDF2==1.26.0
* nltk==3.4.5
* numpy==1.17.2
* Python 3.7.0 |Anaconda 4.3.0 (64-bit)|

## Running localhost

* Run `pip install -r requirements.txt` to install dependencies
* Extract `training-data.zip`

```
python app.py
```

Navigate to http://localhost:5000

If you get permission error in windows machine, run cmd as Administrator.

## Running notebook for algorithm (optional)
Install Anaconda from https://www.anaconda.com/distribution/ and launch jupyter.
* Extract `training-data.zip`
* Place test resumes in `test-resumes` folder
* Open `main.ipynb` in jupyter and run.

## Author

# @Adamantium
