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
      uname = request.form.get("uname")
      conn = mysql.connect()
      cursor = conn.cursor()
      sql = "INSERT INTO users (uname, nickname) VALUES ('" + uname + "', 'test');"
      try:
         cursor.execute(sql)
         conn.commit()
      except pymysql.err.IntegrityError as e:
         print(e)
      conn.close()
      return redirect(url_for('main'))
   else:
      return render_template('signin.html')

@app.route('/main', methods=('GET', 'POST'))
def main():
   return render_template('main.html')

@app.route('/roulette')
def vmd_timestamp():
   return render_template('roulette.html')


if __name__ == '__main__':
   app.run()