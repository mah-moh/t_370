from flask import Flask, render_template, request, redirect, flash
from mysql.connector import connect, Error
from database import Database

app = Flask(__name__)
app.config['SECRET_KEY'] = "very secret"
db = Database()


@app.route('/', methods=['GET', 'POST'])
def Admin():
    if request.method == 'POST':
        id = request.form.get("reg_no")
        data = db.read(id)
        if data is not None:
            return render_template('index.html', data=data[0])
        else:
            flash("Incorrect registration number!")

    return render_template('index.html')

@app.route('/vaccinated/<id>')
def vaccinated(id):
    db.update(id)
    flash("Person Vaccinated!")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)