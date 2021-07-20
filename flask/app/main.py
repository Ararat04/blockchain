from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from block import *

app = Flask(__name__)


@app.route('/')
def index():
    if request.method == 'post':
        lender = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']

        write_block(name=lender, amount=amount, to_whom=borrower)
        return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
