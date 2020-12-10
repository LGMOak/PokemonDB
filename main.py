from flask import Flask, render_template, request
from forms import RegistrationForm, LoginForm
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
def limitResults(result, start=0, end=27):
        return result[start:end]
# limits results to maximum 27 per page 
	
@app.route('/')
def index():
	con = sqlite3.connect('pokemon.db')
	con.row_factory = sqlite3.Row
	# connects flask to sql database

	print("Opened Database Successfully")

	cursor = con.execute("SELECT * FROM pokemon")
	# SQL syntax for selecting all pokemon 

	cursor = cursor.fetchall()

	page = request.args.get('page')

	if not page == None:
		page = int(page)

	if page == None:
	    page = 1
	    cursor = limitResults(cursor)
	else:
	    if page <= 1:
	        page = 1
	        cursor = limitResults(cursor)
	    else:
	        cursor = limitResults(cursor, start=(page-1)*27, end=(page*27))
	# limiting to 27 per page and navigating bteween pages

	return render_template('index.html', cursor=cursor, page=page)

@app.route('/search', methods=['POST'])
def search():
	# search page
	searchcon = sqlite3.connect('pokemon.db')
	searchcon.row_factory = sqlite3.Row

	cursor = searchcon.execute("SELECT * FROM pokemon")

	cursor = cursor.fetchall()

	query = request.form["search"]
	response = searchcon.execute(f"SELECT * FROM pokemon WHERE name like '%{query}%'")
	# get user query and apply it to database and display results

	return render_template('search.html', cursor=response)

@app.route('/IDdesc')
def filter():
	con = sqlite3.connect('pokemon.db')
	con.row_factory = sqlite3.Row
	# connects flask to sql database

	print("Opened Database Successfully")

	cursor = con.execute("SELECT * FROM pokemon ORDER BY pokedexID DESC")
	# SQL syntax for selecting all pokemon 

	cursor = cursor.fetchall()

	page = request.args.get('page')

	if not page == None:
		page = int(page)

	if page == None:
	    page = 1
	    cursor = limitResults(cursor)
	else:
	    if page <= 1:
	        page = 1
	        cursor = limitResults(cursor)
	    else:
	        cursor = limitResults(cursor, start=(page-1)*27, end=(page*27))
	# limiting to 27 per page and navigating bteween pages

	return render_template('index.html', cursor=cursor, page=page)


@app.route('/pokemon/<pokedexID>')
def pokemon(pokedexID):
	# Pokemon specific page
	con = sqlite3.connect('pokemon.db')
	con.row_factory = sqlite3.Row

	print("Opened Database Successfully")

	cursor = con.execute(f"SELECT * FROM pokemon WHERE pokedexID = {pokedexID}")
	# get pokemon ID

	cursor = cursor.fetchall()

	return render_template('pokemon.html', cursor=cursor)

@app.route('/login', methods=['GET'])
def login():
	form = LoginForm()

	return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET'])
def register():
	form = RegistrationForm()

	return render_template('register.html', title='Register', form=form)

@app.route('/dashboard', methods=['GET'])
def dashboard():

	return render_template('dashboard.html')

@app.route('/forgotpasswd', methods=['GET'])
def forgot():

	return render_template('forgot.html')

if __name__ == '__main__':
	app.debug = True
	app.run()