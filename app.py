from flask import Flask, render_template, request, redirect, url_for, session 
from flask_mysqldb import MySQL 
import MySQLdb.cursors 
import re 

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Mydb'
mysql = MySQL(app)
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form['username']
        password= request.form['password']
        cursors = mysql.connection.cursor()
        cursors.execute("INSERT INTO users(username,password) VALUES (%s, %s)", [username,password])
        mysql.connection.commit()
        cursors.close()
        return "success"
    return render_template('index.html')

       
if __name__ == '__main__':
    app.run()