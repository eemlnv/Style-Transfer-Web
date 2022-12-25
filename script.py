from flask import Flask, render_template, request, send_from_directory, flash, redirect
import os
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
from nn import *


app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
style = ""

app.secret_key = 'super secret key'


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/static/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template('index.html')


@app.route("/")
def index(error=''):
	return render_template('index.html', error=error)


@app.route("/success", methods=['POST'])
def upload_file():
	error = 0

	file_names = list(os.walk('./static/images'))[0][2]
	for fn in file_names:
		os.remove(os.path.join('./static/images', fn))

	file_extension = ''
	file_extension2 = ''
	
	file = request.files['file1']

	if not allowed_file(file.filename):
		error = 1
	
	if (file.filename != '') and allowed_file(file.filename):
		img = Image.open(file)
		img = img.convert('RGB')
		img = img.resize((196, 196))
		filename = secure_filename(file.filename)
		file_extension = filename.split('.')[-1]
		img.save(os.path.join(app.config['UPLOAD_FOLDER'], 'content.jpg'))

	file = request.files['file2']
	
	if not allowed_file(file.filename):
		error = 1

	if (file.filename != '') and allowed_file(file.filename):
		img = Image.open(file)
		img = img.convert('RGB')
		img = img.resize((196, 196))
		filename = secure_filename(file.filename)
		file_extension2 = filename.split('.')[-1]
		img.save(os.path.join(app.config['UPLOAD_FOLDER'], 'style.jpg'))

	if error == 1:
		return index(error=error)
	else:
		style_img = image_loader('./static/images/style.jpg')
		content_img = image_loader('./static/images/content.jpg')
		input_img = content_img.clone()
		output = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
												content_img, style_img, input_img)
		tensor_save_rgbimage(output.data[0], app.config['UPLOAD_FOLDER']+'/target.jpg')
		return index(error)
			

if __name__ =="__main__":
	app.run(debug=True)
