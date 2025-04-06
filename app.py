from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    gender = request.form['gender']
    dob = request.form['dob']
    phone = request.form['phone']
    address = request.form['address']
    occupation = request.form['occupation']

    return render_template('result.html', name=name, age=age, email=email, gender=gender, dob=dob, phone=phone, address=address, occupation=occupation)

if __name__ == '__main__':
    app.run(debug=True)
