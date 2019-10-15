from flask import Flask, url_for, render_template, request
import os
import requests
import json
import cx_Oracle
app = Flask(__name__)   

@app.route('/',methods=["POST"])
def inicio():
	users=request.form.get("usuario")
	contraseña=request.form.get("password")
	ip=request.form.get("ip")
	puerto=request.form.get("puerto")
	db=request.form.get("db")
	connect= cx_Oracle.connect(users,contraseña,ip:puerto/db)
	if p.status_code==200:
		return render_template('principal.html')

if __name__ == '__main__':
    app.run()