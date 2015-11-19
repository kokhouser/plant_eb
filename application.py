from flask import Flask,render_template, flash, redirect, session, url_for,request
from app import application, db, models
from app.forms import LoginForm
from sqlalchemy.sql import exists

application = Flask(__name__)
application.debug=True

application.secret_key = 'paradoksu'

@application.route("/")
def blee():
	return redirect(url_for('blah'))

@application.route("/map", methods=['GET', 'POST'])
def blah():
	if request.method == 'POST':
		#print (db.session.query(exists().where(models.Plant.longitude == request.form['longitude'])).scalar())
		#print (request.form['ide'])
		if db.session.query(exists().where(models.Plant.id == request.form['ide'])).scalar():
			#print (db.session.query(exists().where(models.Plant.id == request.form['ide'])).scalar())
			p = db.session.query(models.Plant).\
				filter(models.Plant.id==request.form['ide'])
			if 'delete' in request.form and request.form['delete'] == 'delete':
				print ("Here!")
				for i in p:
					print (i)
					db.session.delete(i)
					db.session.commit()
			else:
				for i in p:
				 	print (i)
				 	i.commonName = request.form['commonName']
				 	i.latinName = request.form['latinName']
				 	db.session.commit()
		else:
			p = models.Plant(commonName = request.form['commonName'], latinName = request.form['latinName'], latitude = request.form['latitude'], longitude = request.form['longitude'])
			db.session.add(p)
			db.session.commit()
	p = models.Plant.query.all()
	plants = [dict(id=row.id, commonName=row.commonName, latinName=row.latinName, latitude=row.latitude, longitude=row.longitude) for row in p]
	plantUnique = []
	for plant in plants:
		if not(plant['commonName'] in plantUnique):
			plantUnique.append(plant['commonName'])
	# Debug statement
	#print plants
	if session.get('logged_in') == True:
		return render_template('map.html', plants = plants, plantUnique = plantUnique)
	else:
		return render_template('map_public.html', plants = plants, plantUnique = plantUnique)

@application.route('/login', methods=['GET', 'POST'])
def bloo():
	form = LoginForm()
	if form.validate_on_submit():
		session['logged_in'] = True
		session['username'] = form.username.data
		print session['username']
		return redirect(url_for('blah'))
	return render_template('login.html', form=form)

@application.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('blah'))

if __name__ == "__main__":
	application.run()