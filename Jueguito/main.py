from elfo import Elfo
from enano import Enano
from humano import Humano
import random

En = Enano("Juan","Enano","Espada",100,20,"Aumento de vida","Fraser")
El = Elfo("Pedro","Elfo","Arco",150,15,"menos 10% vida","Gales")
Hu = Humano("Rojelio","Humano","Pistola",200,20,"Aumento de daño","Brown")

j1 = random.randint(1, 3)
j2 = random.randint(1,3)
while j1 == j2:
    j1 = random.randint(1, 3)
    j2 = random.randint(1,3)

if j1 == 1:
    jugador1 = En
if j1 == 2:
    jugador1 = El
if j1 == 3:
    jugador1 = Hu

if j2 == 1:
    jugador2 = En
if j2 == 2:
    jugador2 = El
if j2 == 3:
    jugador2 = Hu

ronda = 1

if jugador1 == En:
    n = int(input("ingresa un numero del 50 a 100:\n"))
    while n > 100 or n < 50:
        int(input("ingresa un numero del 50 a 100:\n"))
    Enano.aumentarvida(n)

if jugador2 == En:
    n = int(input("ingresa un numero del 50 a 100:\n"))
    while n > 100 or n < 50:
        int(input("ingresa un numero del 50 a 100:\n"))
    Enano.aumentarvida(n)

if jugador1 == El:
    Elfo.quitavida()

if jugador2 == El:
    Elfo.quitavida()

if jugador1 == Hu:
    n = int(input("ingresa un numero del 5 a 15:\n"))
    while n > 15 or n < 5:
        int(input("ingresa un numero del 5 a 15:\n"))
    jugador1.superbono(n)

if jugador2 == Hu:
    n = int(input("ingresa un numero del 5 a 15:\n"))
    while n > 15 or n < 5:
        int(input("ingresa un numero del 5 a 15:\n"))
    jugador2.superbono(n)

