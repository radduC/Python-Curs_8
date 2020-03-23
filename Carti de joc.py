import random
rng = random.Random()

class Carte:
    'Proprietatile necesare crearii unei carti de joc'
    valoare = ['Doi', 'Trei', 'Patru', 'Cinci', 'Sase', 'Sapte', 'Opt', 'Noua', 'Zece', 'Valet', 'Dama', 'Popa', 'As']
    simbol = ['Inima Rosie', 'Caro', 'Inima Neagra', 'Trefla']

    def __init__(self, rang=None, culoare=None):
        if rang == None and culoare == None:
            self.valoare = Carte.valoare[random.randint(0, len(Carte.valoare)-1)]
            self.simbol = Carte.simbol[random.randint(0, len(Carte.simbol)-1)]
        else:
            self.valoare = rang
            self.simbol = culoare

    @classmethod
    def creeaza_carte(cls, nume_carte):
        'Constructor alternativ pentru crearea unei carti anume oferind numele intr-un string ca parametru'
        valoare_carte, simbol_carte = nume_carte.split(' de ')
        return cls(valoare_carte, simbol_carte)

    def __str__(self):
        return f'{self.valoare} de {self.simbol}'

    def simbol_carte(self):
        return self.simbol

    def valoare_carte(self):
        return self.valoare


class Deck:
    'Creeaza un pachet de 52 de carti de joc'

    def __init__(self):
        self.deck = [Carte()]
        for i in range(1, 52):
            carte = Carte()
            j = 0

            while j < i:
                if carte.simbol == self.deck[j].simbol and carte.valoare == self.deck[j].valoare:
                    carte = Carte()
                    j = 0
                else:
                    j += 1

            self.deck.append(carte)
        print('Pachet creat cu succes \n')

    def afiseaza_pachet(self):
        print('Cartile sunt: \n')
        i = 1
        for carte in self.deck:
            print(i, carte)
            i += 1
        print()

    def amesteca_pachet(self):
        'Amesteca cartile'
        rng.shuffle(self.deck)
        print('Cartile amestecate cu succes \n')

        # n = len(self.deck)
        # while n > 1:
        #     n -= 1
        #     k = rng.randrange(n + 1)
        #     carte = self.deck[k]
        #     self.deck[k] = self.deck[n]
        #     self.deck[n] = carte

    def elimina_carte(self, carte):
        'Elimina o carte din pachet'

        if type(carte) is str:  # eliminare dupa nume
            valoare_carte, simbol_carte = carte.split(' de ')

            for c in self.deck:
                if c.valoare == valoare_carte and c.simbol == simbol_carte:
                    self.deck.remove(c)
                    print(f'[{carte}] eliminata \n')
                    return
            print(f'[{carte}] tip invalid de carte \n')

        elif type(carte) is int:  # eliminare dupa index
            if carte in range(len(self.deck)):
                self.deck.pop(carte)
                print(f'[{self.deck[carte]}] eliminata \n')
            else:
                print('Index invalid \n')

        elif type(carte) is Carte:
            for c in self.deck:
                if c.valoare == carte.valoare and c.simbol == carte.simbol:
                    self.deck.remove(c)
                    print(f'[{carte}] eliminata \n')

        else:
            print(f'[{carte}] tip invalid de carte \n')

    def adauga_carte(self, nume_carte):
        'Adauga carte daca pachetul nu e plin'        
        if len(self.deck) < 51:
            valoare_carte, simbol_carte = nume_carte.split(' de ')
            if valoare_carte in Carte.valoare and simbol_carte in Carte.simbol:            
                for c in self.deck:
                    if c.valoare == valoare_carte and c.simbol == simbol_carte:
                        print(f'[{nume_carte}] se afla deja in pachet pe pozitia {self.deck.index(c) + 1} \n')
                        return                        
                self.deck.append(Carte(valoare_carte, simbol_carte))
                print(f'[{nume_carte}] adaugata cu succes \n')
            else:
                print(f'[{nume_carte}] nume invalid de carte \n')
        else:
            print('Pachetul este plin, nu se pot adauga carti.')

def Curs_7_Ex_1():
    deck = Deck()

    deck.afiseaza_pachet()
    deck.amesteca_pachet()
    deck.afiseaza_pachet()

    deck.elimina_carte(30)
    deck.elimina_carte(20)
    deck.adauga_carte('As de Caro')
    
    deck.elimina_carte(60)    
    deck.afiseaza_pachet()


if __name__ == "__main__":

    deck = Deck()

    deck.afiseaza_pachet()
    deck.amesteca_pachet()
    deck.afiseaza_pachet()

    # deck.elimina_carte('As de Caro')
    deck.elimina_carte(30)
    deck.elimina_carte(20)
    deck.adauga_carte('As de Caro')
    # deck.adauga_carte('As de Caro')
    deck.elimina_carte(60)
    # deck.elimina_carte('Popa de Romb')
    deck.afiseaza_pachet()