from flask import Flask, render_template, request
from mysql.connector import connect, Error
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/', methods=['GET', 'POST'])
def Admin():
    if request.method == 'POST':
        id = request.form.get("reg_no")
        data = db.read(id)
        return render_template('index.html', data=data[0])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)