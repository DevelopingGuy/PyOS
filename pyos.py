
#Inizio

def start():
    print('''Welcome to the NoNameOS
    type Help for a list of program and command/action''')

    choose1 = input('$ ')

    if choose1 == 'help': #Aggiungere un sistema di login | Istruzioni poco chiare
        print('''First of all, type 'help' in every screen for a visual of every command.
        use 'ls' for the list of file
        use 'cd' for moving in another folder
        use 'cd ..' for moving to the last folder
        use './programname' for opening a program''')
        normal()

#Menu

def normal():
    choose2 = input('$ ')
    if choose2 == 'ls':
        print('''programs   photos  audio   music   .code''')
    if choose2 == 'cd programs':
        print('''Calculator  ''') #Aggiungere altri programmi

#Applicazioni

def CalculatorApp():
    print('Ancora in costruzione...')
    #Da Fare


start()