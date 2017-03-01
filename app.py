from flask import Flask, render_template,redirect, json, request,jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL(app)
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'api_flask'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def index():
	gold = 1
	silver = 2
	con=mysql.connect()
	cursor=con.cursor()
	cursor.callproc('ListaIndex',(gold,))
	an_gold = cursor.fetchall()
	cursor.callproc('ListaIndex',(silver,))
	an_silver = cursor.fetchall()
	return render_template("index.html", golds = an_gold, silvers = an_silver)

@app.route('/api/list', methods=['GET'])
def list():
	
	cat = request.args.get("categoria")
	con=mysql.connect()
	cursor=con.cursor()
	cursor.callproc('ListaAnuncios',(cat,))
	categorias = cursor.fetchall()

	return render_template('lista.html', items = categorias)

if __name__ == '__main__':
	app.run(debug=True)