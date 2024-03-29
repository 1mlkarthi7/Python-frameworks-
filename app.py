from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
#from werkzeug.datastructures import  FileStorage
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('file.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True, port=8907)
