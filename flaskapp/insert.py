from flask import Flask,request
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
 
@app.route("/")
def hello():
    return "Welcome to Python Flask App!"
@app.route("/Insert")
def Insert():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    con=mysql.connect()
    cursor.execute("insert into User(userName,password)  values('"+ username +"','" + password +"')")
    con.commit()
    return "Insert Successfully"
    
if __name__ == "__main__":
    app.run()

