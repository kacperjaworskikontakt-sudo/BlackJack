#gra w blackjacka
import random
class Blackjack:

    def __init__(self):
        pass

    def krupier(self):
        print("")
        print("Rozdawanie kart...")
        print("")
        print("Twoje karty:")
        print("")
        karta1 = random.randint(2,11)
        karta2 = random.randint(2,11)
        print(f"[{karta1}♠] [{karta2}♥]")
        print(f"Suma punktów: {karta1 + karta2}")
        print("")


    def start(self):
        self.saldo = 1000
        print("====================================")
        print("           ♠ BLACKJACK ♥")
        print("====================================")
        print(f"Twoje saldo wynosi: {self.saldo}$")
        blackjack.gra()

    def gra(self):
        self.stawka = int(input("Podaj stawke: "))
        self.saldo -= self.stawka
        blackjack.krupier()

#rozdawanie kart
#karty moje i krupiera
#punty 
#czy kontynuacja
#wygrywasz/przegrywasz
#statystyki


print("test")



blackjack = Blackjack()
blackjack.start()
