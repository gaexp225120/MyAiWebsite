import os
from flask import Flask, request, render_template, url_for, redirect
import FaceRecog_Advanced_Library as FA
import FaceRecog_Basic_Library 
import FaceRecog_FaceList_Library 

app = Flask(__name__)
app.config["DEBUG"] = True

imgSavePath = 'C:/Users/user/Desktop/Faceapi/Flask/test/Pictures/imgno'
tempFileName = 1

@app.route('/')
def index():
	return render_template('index.html')




@app.route("/showEmotions", methods=['POST'])

def showEmotions():
	global tempFileName
	str_targetImg=request.values['inputImage']  
	detectMode=2
	str_filename=imgSavePath+str(tempFileName)+'.jpg'
	try:
		FA.DetectFace(str_targetImg, detectMode ,str_filename)
		tempFileName=tempFileName+1
	except AttributeError:
		print("Couldn't save image {}")
	return redirect(url_for('index'))


@app.route("/showAge", methods=['POST'])

def showAge():	
	global tempFileName
	str_targetImg=request.values['inputImage']  
	detectMode=1
	str_filename=imgSavePath+str(tempFileName)+'.jpg'
	try:
		FA.DetectFace(str_targetImg, detectMode ,str_filename)
		tempFileName=tempFileName+1
	except AttributeError:
		print("Couldn't save image {}")
	return redirect(url_for('age'))

# @app.route("/handleUpload", methods=['POST'])

# def handleUpload():
#     if 'photo' in request.files:
#         photo = request.files['photo']
#         if photo.filename != '':            
#             photo.save(os.path.join('C:/Users/user/Desktop/Faceapi/Flask/test/Pictures', photo.filename))
#     return redirect(url_for('index'))

@app.route('/age')

def age():
	return render_template('age.html')

@app.route('/')

def back():
	return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
