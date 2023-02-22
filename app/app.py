from flask import Flask, render_template, request, url_for, flash, redirect, session
from flaskext.mysql import MySQL
import pymysql
import sys

app = Flask(__name__)
mysql = MySQL()
app.secret_key = 'poopoopeepee'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = "poop"
app.config['MYSQL_DATABASE_DB'] = 'myapp'
if sys.platform == 'linux':
   app.config['MYSQL_DATABASE_HOST'] = 'db'
elif sys.platform == 'win32':
   app.config['MYSQL_DATABASE_HOST'] = 'localhost'
else:
   print('Boi what is you running this app on??')
   exit

mysql.init_app(app)
import games.roulette

winning_number = 38
winning_color = 'green'

connection = mysql.connect()
cursor = connection.cursor()
      
@app.route('/', methods=('GET', 'POST'))
def home():
   if request.method == "POST": 
      username = request.form.get("uname")
      print(username, file=sys.stderr)
      cursor.execute("SELECT * FROM accounts WHERE username = %s", username)
      print('cursor executed the query.')
      connection.commit()
      print('connection commited the query')
      account = cursor.fetchone()
      print(account)
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
      return render_template('roulette.html', account=account[1], num_of_chips=account[4], last_spin_number=winning_number, last_winning_color=winning_color.capitalize())
   else:
      return redirect('/')    
   
@app.route('/roulette_simulation', methods=['GET', 'POST'])
def roulette_simulation():
   if request.method == "GET":
      if 'loggedin' in session:
         return render_template('roulette_simulation.html')
      else:
         return redirect('/')    
   else:
      print('post method received.')

@app.route('/makeRouletteBet', methods=['POST'])
def makeRouletteBet():
   if 'loggedin' in session:
      bets =  request.get_json()['bets']
      # roullete logic to see if i win
      global winning_number, winning_color
      winning_number, winning_color = games.roulette.check_bets(bets, cursor, connection, session)
      if winning_number == 37:
         winning_number = '0'
      if winning_number == 38:
         winning_number = '00'
      return redirect('roulette')
   else:
      return redirect('/')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')