from flask import Flask, render_template, request, url_for, flash, redirect
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234qwer!@#$QWER'
app.config['MYSQL_DATABASE_DB'] = 'myapp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/', methods=('GET', 'POST'))
def home():
   if request.method == "POST":
      # Check if user is in DB
      uname = request.form.get("uname")

      conn = mysql.connect()
      cursor = conn.cursor()
      sql = "INSERT INTO users (uname, nickname) VALUES ('" + uname + "', 'test');"
      try:
         cursor.execute(sql)
         conn.commit()
      except pymysql.err.IntegrityError as e:
         if "Duplicate entry" in e:
            print(e)
      # except:
      #    print('poop')
      conn.close()
      
      # If not create a new user
      # If login
      return redirect(url_for('poop'))
   return render_template('index.html')

@app.route('/poop', methods=('GET', 'POST'))
def poop():
   return render_template('poop.html')


if __name__ == '__main__':
   
   app.run()