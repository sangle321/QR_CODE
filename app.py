from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import db
import json
import create_QR as CR

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route("/")
def main():
	return render_template('home.html')

# @app.route("/err")
# def main():
# 	return "<h1>Mã sinh viên bạn nhập vào bị trùng</h1>"


@app.route('/index', methods=['POST'])
def create_qrcode_student():
	_id = request.form['id']
	_name = request.form['name']
	if db.check_masv(_id) == None:
		link_qr = CR.create_QR(_id )
		db.insert_QR(_id, _name, link_qr)
		return render_template('home.html')
	return render_template('home.html')

@app.route('/getAll', methods=['GET'])
def get_all():
	list_student = db.select_all_student()
	return render_template('index.html', len = len(list_student) , students = list_student)

if __name__ == '__main__':
	app.run(use_reloader = True, debug=True)