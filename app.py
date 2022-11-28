from flask import Flask, render_template, request, url_for, flash, redirect, session
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
mysql = MySQL()
app.secret_key = 'poopoopeepee'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234qwer!@#$QWER'
app.config['MYSQL_DATABASE_DB'] = 'myapp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/', methods=('GET', 'POST'))
def home():
   if request.method == "POST": 
      connection = mysql.connect()
      cursor = connection.cursor()
      username = request.form.get("uname")
      cursor.execute("SELECT * FROM accounts WHERE username = %s", username)
      connection.commit()
      account = cursor.fetchone()
      if account:
         # Create session data, we can access this data in other routes
         session['loggedin'] = True
         session['id'] = account[0]
         session['username'] = account[1]
         # Redirect to home page
         return render_template('main.html')
      else:
         cursor.execute("INSERT INTO accounts (id, username, password, email, chips) VALUES (NULL, %s, NULL, NULL, %s)", (username, 100))
         connection.commit()
         return render_template('signin.html', newaccount=username)
   if request.method == "GET": 
      return render_template('signin.html')

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect('/')

@app.route('/main', methods=('GET', 'POST'))
def main():
   if 'loggedin' in session:
      return render_template('main.html')
   else:
      return redirect('/')

@app.route('/roulette')
def roulette():
   if 'loggedin' in session:
      return render_template('roulette.html')
   else:
      return redirect('/')      


if __name__ == '__main__':
   app.run()