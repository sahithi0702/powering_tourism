from flask import Flask,request,render_template,session,redirect,url_for
import smtplib
app= Flask(__name__)
app.secret_key = "super secret key "
import sqlite3
l=[]
p=[]

@app.route('/')
def ho():
	return render_template("home.html")

@app.route('/con')
def abo() :
	return render_template("contact.html")

@app.route('/tlog')
def tlog() :
	return render_template("Tlog.html")

@app.route('/blog')
def blog() :
	return render_template("Blog.html")

@app.route('/abo')
def abou():
	return render_template("about.html")

@app.route('/sig') 
def sig():
	return render_template("signup.html")

@app.route('/logo')
def log():
	return render_template("home.html")

@app.route('/hom')
def home():
	return render_template('home.html')

@app.route("/bussdeal")
def deal():
	return render_template("mail.html")
		
@app.route("/delhi")
def delhi():
	return render_template("delhi.html")

@app.route("/goa")
def goa():
	return render_template("goa.html")

@app.route("/gujarath")
def gujarath():
	return render_template("gujarath.html")

@app.route("/himachal")
def himachal():
	return render_template("himachal.html")

@app.route("/insurance")
def insurance():
	return render_template("insurance.html")

@app.route("/signm_c",methods=['POST'])
def signm_c() :
	fn = request.form.get("fn")
	ln = request.form.get("ln")
	e_id = request.form.get("e_id")
	pa = request.form.get("pa")
	conn = sqlite3.connect('database1.db')
	conn.execute('CREATE TABLE IF NOT EXISTS customer (name TEXT, email TEXT primary key, password TEXT)')
	cur = conn.cursor() 
		
	cur.execute("INSERT INTO customer (name,email,password) VALUES (?,?,?)",(fn,e_id,pa))
	conn.commit()
	message="thanks for signing up !! we have successfully recorded your response we will get back to you as soon as possible!"
	server=smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login("pausethemoment255@gmail.com","pausethemoment")
	server.sendmail("pausethemoment255@gmail.com",e_id,message)
	l.append(f"{e_id}")
	p.append(f"{pa}")
	return render_template('signmail.html',l=l,p=p)

@app.route('/sigt') 
def sigt():
	return render_template("signup_t.html")


@app.route("/signm",methods=['POST'])
def signm() :
	fn = request.form.get("fn")
	ln = request.form.get("ln")
	e_id = request.form.get("e_id")
	pa = request.form.get("pa")
	conn = sqlite3.connect('database1.db')
	conn.execute('CREATE TABLE IF NOT EXISTS tourists (name TEXT, email TEXT primary key, password TEXT)')
	cur = conn.cursor() 
		
	cur.execute("INSERT INTO tourists (name,email,password) VALUES (?,?,?)",(fn,e_id,pa))
	conn.commit()
	message="thanks for signing up !! we have successfully recorded your response we will get back to you as soon as possible!"
	server=smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login("pausethemoment255@gmail.com","pausethemoment")
	server.sendmail("pausethemoment255@gmail.com",e_id,message)
	l.append(f"{e_id}")
	p.append(f"{pa}")
	return render_template('signmail.html',l=l,p=p)



@app.route("/homer", methods = ['POST', 'GET'])
def tou():
	if request.method == "POST":
		emai = request.form['mail']
		passwor = request.form['pass']
		conn = sqlite3.connect('database1.db')
		conn.execute('CREATE TABLE IF NOT EXISTS tourists (name TEXT, email TEXT primary key, password TEXT)')
		cur = conn.cursor() 
		
		query = "select password from tourists where email = '" + emai + "'"
		db_mail = cur.execute(query).fetchall()
		#print(db_mail[0])
		if len(db_mail)>=1 :
			if passwor in db_mail[0] :
				print('login successful')
				return render_template("home.html",x = emai)
			else :
				return "wrong password"
		else :
			return "please register"


@app.route('/homb', methods = ['POST', 'GET'])
def bus():
	if request.method == "POST":
		emai = request.form['mail']
		passwor = request.form['pass']
		conn = sqlite3.connect('database1.db')
		conn.execute('CREATE TABLE IF NOT EXISTS customers (name TEXT, email TEXT primary key, password TEXT)')
		cur = conn.cursor() 
		
		query = "select password from customer where email = '" + emai + "'"
		print(query)
		db_mail = cur.execute(query).fetchall()
		#print(db_mail[0])
		if len(db_mail)>=1 :
			if passwor in db_mail[0] :
				print('login successful')
				return render_template("bussiness.html")
			else :
				return "wrong password"
		else :
			return "please register"

# 14 - 05 - 2022 

@app.route('/clientdetails', methods = ['POST','GET'])
def clientdetails():
	if request.method == "POST":
		nameOfEnterprise = request.form['nameofE']
		mailingAddress   = request.form['mailingAdd']
		city             = request.form['cit']
		state            = request.form['stat']
		Zipcode          = request.form['zipcod']
		phoneno          = request.form['mobileno']
		fax              = request.form['fa']
		bussinessType    = request.form['bussinessTyp']
		taxid            = request.form['taxi']
		gstin            = request.form['GSTI']
		ContractAmount   = request.form['contractAmoun']
		ContractDuration = request.form['ContractDuration']
		conn = sqlite3.connect('database1.db')
		conn.execute('CREATE TABLE IF NOT EXISTS Client_Info (nameOfEnterprise TEXT, mailingAddress TEXT, city TEXT , state TEXT , Zipcode TEXT,phoneno TEXT,fax TEXT,bussinessType TEXT,taxid TEXT, gstin TEXT,ContractAmount TEXT,ContractDuration TEXT)')
		cur = conn.cursor() 	
		cur.execute("INSERT INTO Client_Info (nameOfEnterprise,mailingAddress,city,state,Zipcode,phoneno,fax,bussinessType,taxid,gstin,ContractAmount,ContractDuration) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(nameOfEnterprise,mailingAddress,city,state,Zipcode,phoneno,fax,bussinessType,taxid,gstin,ContractAmount,ContractDuration))
		conn.commit()



if __name__ == '__main__' :
	app.run(debug=True)