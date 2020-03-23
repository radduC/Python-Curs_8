from flask import Flask, request, render_template, jsonify
import Deck_of_cards, Expresii_Regulate

app = Flask(__name__)

pachet = Deck_of_cards.Deck()
data = []

@app.route('/')
def hello_world(): 
    return str('<p><h1>Hello World!</h1>')


@app.route('/users/names')
def users():
    names = ['Ion', 'Mihai', 'Diana']
    return f'{names[0]} \n {names[1]} \n {names[2]}'


@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'


@app.route('/<parametru>')
def Curs_7(parametru):
    if parametru == '1':
        return str(pachet.cards)
        # return render_template('Deck.html', deck = pachet)
    elif parametru == 'shuffle':
        pachet.shuffle()
        return render_template('Deck.html', deck = pachet)
    elif parametru == 'deal':        
            return str(pachet.deal_card())
    elif parametru == '2':
        return str(Expresii_Regulate.Curs_7_2())
    else:
        return '<h2>Resursa necunoscuta</h2>'            
       
    
@app.route('/list', methods = ['GET', 'POST'])
def post():
    if request.method == 'POST':
        print(request.form['key'])              
        data.append(int(request.form['key']))
        return str(data)
    elif request.method == 'GET':
        return str(data)

    

if __name__ == '__main__':
    app.run(debug='True')