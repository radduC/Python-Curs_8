from flask import Flask, request
app = Flask(__name__)

@app.route('/square', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        number = int(request.form['value'])
        return str(number**2)
    else:
        return 'Use POST method for squaring the number'

if __name__ == '__main__':
    app.run(debug='True')