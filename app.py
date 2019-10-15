from flask import Flask, url_for, render_template, request
import os
import requests
import json
import cx_Oracle
app = Flask(__name__)   

@app.route('/',methods=["GET","POST"])
def inicio():
	if request.method=="GET":
		return render_template('principal.html')
	else:
		users=request.form.get("usuario")
		contraseña=request.form.get("password")
		ip=request.form.get("ip")
		puerto=request.form.get("puerto")
		db=request.form.get("db")
		ident=(usuario,password,ip+":"+puerto+"/"+db)
		connect= cx_Oracle.connect(ident[0],ident[1],ident[2])
		if connect.status_code==200:
			return render_template('principal.html')
		else:
			return print("Los datos introducidos son incorrectos")

if __name__ == '__main__':
    app.run()