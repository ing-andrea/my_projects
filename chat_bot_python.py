# Project: Chat Bot in Python

# Chat Bot stages:
# Stage 1: Chatty Bot welcomes you
# Stage 2: Print your name
# Stage 3: Guess the age
# Stage 4: Learning numbers
# Stage 5: Multiple choice

print('Ciao! Il mio nome è AndreaBot.')
print('Sono stato creato nel 2021.')
print('Ricordami il tuo nome, grazie.')

nome = input('Inserisci il tuo nome: ')

print('Che bel nome che hai, ' + nome)
print('Fammi indovinare la tua età.')
print('Inserisci i resti della divisione della tua età per 3, 5 e 7.')

x = int(input())
y = int(input())
z = int(input())
age = (x * 70 + y * 21 + z * 15) % 105
print('La tua età è: ' + str(age) +'; è un buon momento per iniziare a programmare!')
print('Ora ti dimostrerò che posso contare fino a qualsiasi numero tu voglia.')

number = int(input('Inserisci un numero: '))
i = 0

while (i <= number):
    print (i,'!')
    i = i + 1

input('Press Enter to continue...')

print("Mettiamo alla prova le tue conoscenze di programmazione.")
print ('Why do we use methods?')
print ('1. To repeat a statement multiple times.')
print ('2. To decompose a program into several small subroutines.')
print ('3. To determine the execution time of a program.')
print ('4. To interrupt the execution of a program.')

risposta_esatta = 2

while True:
    number = eval(input('Inserisci la risposta: '))
    if number == risposta_esatta:
        print ('Bravo, risposta esatta!')
        break
    else:
        print ('Per favore, prova ancora.')

def end():
    print('Congratulazioni, buona giornata!')
end()
