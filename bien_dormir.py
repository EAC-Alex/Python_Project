import os, subprocess, re
from time import sleep
from datetime import datetime, timedelta

print(
"""
-----------------------------
Bienvenue dans bien_dormir.py
-----------------------------

         ______
      .-'` .    `'-.
    .'  '    .---.  '.
   /  '    .'     `'. \  
  ;  '    /          \|   
 :  '  _ ;            `   
;  :  /(\ \       
|  .       '.
|  ' /     --'
|  .   '.__\
;  :       /
 ;  .     |            ,
  ;  .    \           /|
   \  .    '.       .'/
    '.  '  . `'---'`.'
      `'-..._____.-`

Ce script prend en compte qu'il faut 15 min en moyenne pour s'endormir.
Il faut en général 5 à 6 cycles (un cycle = 90 min) pour une bonne nuit.

""")

sleep(3)

print(
"""
----------
   MODE
----------

1) Choisir l'heure à laquelle je veux me réveiller et recevoir l'heure à laquelle je devrais dormir.
2) Allez dormir maintenant et recevoir l'heure ou je devrais me lever.

""")

mode_choice = input("Votre mode : ")

if mode_choice == "1":
    wakeup_hour = input("A quelle heure voulez vous vous réveillez ? : ")
    wakeup_minutes = input("A quelle minutes voulez-vous vous réveillez ? : ")
    complete_time = "%s:%s:00" % (wakeup_hour, wakeup_minutes)

    sleep_time_1 = str(datetime.strptime(complete_time,"%H:%M:%S") - datetime.strptime("09:15:00","%H:%M:%S"))
    sleep_time_2 = str(datetime.strptime(complete_time,"%H:%M:%S") - datetime.strptime("07:45:00","%H:%M:%S"))
    sleep_time_3 = str(datetime.strptime(complete_time,"%H:%M:%S") - datetime.strptime("06:15:00","%H:%M:%S"))
    sleep_time_4 = str(datetime.strptime(complete_time,"%H:%M:%S") - datetime.strptime("04:45:00","%H:%M:%S"))

    liste = [sleep_time_1, sleep_time_2, sleep_time_3, sleep_time_4]

    print("\nVoici les heures ou vous devriez allez vous coucher : \n")
    for i in liste:
        i = re.sub("-1 day, ", "", i)
        print("---> ", i)

    input()

elif mode_choice == "2":
    wakeup_time_1 = datetime.today() + timedelta(hours=4, minutes=45)
    wakeup_time_2 = datetime.today() + timedelta(hours=6, minutes=15)
    wakeup_time_3 = datetime.today() + timedelta(hours=7, minutes=45)
    wakeup_time_4 = datetime.today() + timedelta(hours=9, minutes=15)

    liste = [wakeup_time_1, wakeup_time_2, wakeup_time_3, wakeup_time_4]

    print("\nVoici les heures ou vous devriez vous réveiller : \n")
    for i in liste:
        i = i.strftime("%H h %M")
        print("---> ", i)

    input("Appuyer sur Enter pour quitter...")

else:
    print("\nCe mode n'existe pas !")

    print("\nRelancement du script...")
    sleep(3)

    path = os.path.realpath(__file__)
    subprocess.run(["python", path])