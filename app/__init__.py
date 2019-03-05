
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


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
		l11 = request.form['l11']
		
		sum = int(l1)+int(l2)+int(l3)+int(l4)+int(l5)+int(l6)+int(l7)+int(l8)+int(l9)+int(l10)+int(l11);
	return render_template("liver.html", agee=int(sum))

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
		sum = int(d1)+int(d2)+int(d3)+int(d4)+int(d5)+int(d6)+int(d7)+int(d8);
	return render_template("diabetes.html", agee=int(sum))





if __name__ == '__main__':
    app.run()

    






