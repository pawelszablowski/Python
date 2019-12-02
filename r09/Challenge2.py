### Gra w wojne

import gry, karty, datetime

response = None
while response != "n":
    print("Witaj w grze wojna")
    talia = karty.Deck()
    talia.populate()
    talia.shuffle()
    print(talia,"\n")
    now = datetime.datetime.now()
    print("Now is ", now.strftime("%d-%m-%Y")," at ", now.strftime("%H:%M:%S\n"))
    print("a, dokładnie :",  now )
    
    response = gry.ask_yes_no("\nCzy chcesz zagrać ponownie? (t/n): ")
