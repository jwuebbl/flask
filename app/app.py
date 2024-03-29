from flask import Flask, make_response, render_template, request, url_for, flash, redirect, session, jsonify
from flaskext.mysql import MySQL
import pymysql
import sys
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mysql = MySQL()
app.secret_key = 'poopoopeepee'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = "poop"
app.config['MYSQL_DATABASE_DB'] = 'myapp'
if sys.platform == 'linux':
   app.config['MYSQL_DATABASE_HOST'] = 'mysql_db'
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
   if 'loggedin' in session:
      return redirect(url_for(' '))
   else:
      if request.method == "GET":
         needToSignIn = request.args.get('needToSignIn')
         return render_template('signin.html', needToSignIn=needToSignIn)
      if request.method == "POST":
         username = request.form.get("uname")
         cursor.execute("SELECT * FROM accounts WHERE username = %s", username)
         connection.commit()
         account = cursor.fetchone()
         if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            return redirect(url_for('menu'))
         else:
            cursor.execute("INSERT INTO accounts (id, username, password, email, chips) VALUES (NULL, %s, NULL, NULL, %s)", (username, 100))
            connection.commit()
            newaccount = username
            return render_template('signin.html', newaccount=newaccount)

@app.route('/menu', methods=('GET', 'POST'))
def menu():
   if 'loggedin' in session:
      return render_template('menu.html')
   else:
      needToSignIn = True
      return redirect(url_for('home', needToSignIn=needToSignIn))

@app.route('/submitLeagueGame', methods=['OPTIONS', 'GET', 'POST'])
def submitLeagueGame():
   if 'loggedin' in session:
      if request.method == "OPTIONS":
         response = make_response()
         response.headers.add("Access-Control-Allow-Origin", "*")
         response.headers.add("Access-Control-Allow-Headers", "*")
         response.headers.add("Access-Control-Allow-Methods", "*")
         return response
      if request.method == "POST":
         char = request.json['char']
         kills = request.json['kills']
         deaths = request.json['deaths']
         assists = request.json['assists']
         winLoss = request.json['winLoss']
         cursor.callproc('addLeageGame', [int(session['id']), str(char), int(kills), int(deaths), int(assists), str(winLoss)])
         connection.commit()
         response = make_response('')
         return response
      if request.method == "GET":
         return render_template('lolKda.html')
   else:
      needToSignIn = True
      return redirect(url_for('home', needToSignIn=needToSignIn))


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
      print(request.method + " Received.")

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
   
@app.route('/username')
def username():
   if 'loggedin' in session:
      username = session['username']
      response = {'username': username}
      return jsonify(response)
   else:
      return 400

@app.route('/leagueScoreBoard')
def leagueScoreBoard():
   query = "SELECT * FROM leagueGames WHERE accountId = " + str(session['id']) + " ORDER BY gameNum DESC LIMIT 5;"
   print(query)
   cursor.execute(query)
   connection.commit()
   response = cursor.fetchall()
   # one record schema: gameNum, accountId, char, kills, deaths, assists, win/loss, datetime
   # one record example: (5, 4, 'Akali', 0, 0, 0, 'L', datetime.datetime(2023, 5, 9, 20, 21, 43))
   results = []
   for game in response:
      results.append(game)
   return results
   
@app.route('/logout')
def logout():
   session.pop('loggedin')
   session.pop('id')
   session.pop('username')
   return redirect(url_for('home'))

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
