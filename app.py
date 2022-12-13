from flask import Flask, render_template, request, url_for, flash, redirect, session
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
mysql = MySQL()
app.secret_key = 'poopoopeepee'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = "1234qwer!@#$QWER"
app.config['MYSQL_DATABASE_DB'] = 'myapp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

connection = mysql.connect()
cursor = connection.cursor()

@app.route('/', methods=('GET', 'POST'))
def home():
   if request.method == "POST": 
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
      cursor.execute("SELECT * FROM accounts WHERE username = %s", session['username'])
      connection.commit()
      account = cursor.fetchone()
      return render_template('roulette.html', account=account[1], num_of_chips=account[4])
   else:
      return redirect('/')    

@app.route('/roulette2')
def roulette2():
   if 'loggedin' in session:
      cursor.execute("SELECT * FROM accounts WHERE username = %s", session['username'])
      connection.commit()
      account = cursor.fetchone()
      return render_template('roulette2.html', account=account[1], num_of_chips=account[4])
   else:
      return redirect('/')     

@app.route('/makeRouletteBet', methods=['POST'])
def makeRouletteBet():
   print('request made')
   bets =  request.get_json()['bets']
   for bet in bets:
      print(bet)

   cursor.execute("SELECT * FROM accounts WHERE username = %s", session['username'])
   connection.commit()
   account = cursor.fetchone()
   # roullete logic to see if i wins
   return render_template('roulette.html', account=account[1], num_of_chips=account[4])




if __name__ == '__main__':
   app.run()