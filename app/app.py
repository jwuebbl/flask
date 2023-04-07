from flask import Flask, make_response, render_template, request, url_for, flash, redirect, session, jsonify
from flaskext.mysql import MySQL
import pymysql
import sys
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
         return render_template('signin.html')
   if request.method == "GET": 
      # index.html is the angular webpage.
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
      print('/roulette_simulation post method received.')

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
   
@app.route('/submitLeagueGame', methods=['OPTIONS', 'GET', 'POST'])
@cross_origin()
def submitLeagueGame():
   if 'loggedin' in session:
      if request.method == "OPTIONS":
         print('options')
         response = make_response()
         response.headers.add("Access-Control-Allow-Origin", "*")
         response.headers.add("Access-Control-Allow-Headers", "*")
         response.headers.add("Access-Control-Allow-Methods", "*")
         return response
      if request.method == "POST":
         print('post')
         char = request.json['char']
         kills = request.json['kills']
         deaths = request.json['deaths']
         assists = request.json['assists']
         cursor.callproc('addLeageGame', [int(session['id']), str(char), int(kills), int(deaths), int(assists)])
         connection.commit()
         response = make_response('')
         return response
      else:
         return render_template("LoLKda.html")


   

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
