from flask import Flask,render_template,request
from flaskext.mysql import MySQL
import secrets


secret_key = secrets.token_hex(16)


mysql = MySQL()
app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = "new_password"
app.config['MYSQL_DATABASE_DB'] = 'wallet'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route('/',methods=['GET','POST'])
def index():
   if request.method=='POST':
      phno=request.form['phno']
      password=request.form['password']
      amnt=request.form['amount']
      if int(amnt) <200:
         error="<h1>Insufficient Amount Need Minimunm 200 To Create an Account</h1>"
         return error
      conctn=mysql.connect()
      db=conctn.cursor()

      db.execute('INSERT INTO User VALUES(%s,%s,%s)',(phno,password,amnt))
      conctn.commit()
      db.close()
      return render_template('index.html')

   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)

