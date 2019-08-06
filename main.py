import os
from flask import Flask, request, render_template, url_for, redirect
import FaceRecog_Advanced_Library as FA
import FaceRecog_Basic_Library 
import FaceRecog_FaceList_Library 

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
	return render_template('index.html')




@app.route("/detect", methods=['POST'])

def detect():	
	str_targetImg=request.values['inputImage']  
	detectMode=0
	try:
		FA.DetectFace(str_targetImg, detectMode)
	except AttributeError:
		print("Couldn't save image {}")
	return redirect(url_for('index'))


@app.route("/handleUpload", methods=['POST'])

def handleUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':            
            photo.save(os.path.join('C:/Users/user/Desktop/Faceapi/Flask/test/Pictures', photo.filename))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
