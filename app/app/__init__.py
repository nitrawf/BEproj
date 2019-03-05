
from flask import Flask, render_template, request
from Modules import diabetus_tester,liver_tester


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/liver')
def liver():
    return render_template("liver.html")

@app.route('/send2',methods=['GET','POST'])
def send2(): 
	if request.method == 'POST':

		l1 = request.form['l1']
		l2 = request.form['l2']
		l3 = request.form['l3']
		l4 = request.form['l4']
		l5 = request.form['l5']
		l6 = request.form['l6']
		l7 = request.form['l7']
		l8 = request.form['l8']
		l9 = request.form['l9']
		l10 = request.form['l10']
	
		mylist=[]
		mylist.append(float(l1))
		if l2 == "f":
			mylist.append(float(0))
		else:
			mylist.append(float(1))
		mylist.append(float(l3))
		mylist.append(float(l4))
		mylist.append(float(l5))
		mylist.append(float(l6))
		mylist.append(float(l7))
		mylist.append(float(l8))
		mylist.append(float(l9))
		mylist.append(float(l10))


	return render_template("liver.html", agee=round(liver_tester.result_liver(mylist).item(0)*100,2))



@app.route('/heart')
def heart():
    return render_template("heart.html")

@app.route('/diabetes')
def diabetes():
    return render_template("diabetes.html")

@app.route('/send1',methods=['GET','POST'])
def send1(): 
	if request.method == 'POST':

		d1 = request.form['d1']
		d2 = request.form['d2']
		d3 = request.form['d3']
		d4 = request.form['d4']
		d5 = request.form['d5']
		d6 = request.form['d6']
		d7 = request.form['d7']
		d8 = request.form['d8']
		mylist=[]
		mylist.append(float(d1))
		mylist.append(float(d2))
		mylist.append(float(d3))
		mylist.append(float(d4))
		mylist.append(float(d5))
		mylist.append(float(d6))
		mylist.append(float(d7))
		mylist.append(float(d8))


	return render_template("diabetes.html", agee=round(diabetus_tester.result_diabetus(mylist).item(0)*100,2))



if __name__ == '__main__':
    app.run()

    






