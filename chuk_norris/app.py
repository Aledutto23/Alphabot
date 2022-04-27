import requests

scelta = input("inserire un'opzione: ")

if int(scelta) == 0:
    r = requests.get('https://api.chucknorris.io/jokes/random')
    r = r.json()
    print(r["value"])

elif int(scelta) == 1:
    scelta = input("scegliere una delle seguenti categorie: animal, career, celebrity, dev, explicit, fashion, food, history, money, movie, music, political, religion, science, sport, travel: ")
    r = requests.get(f'https://api.chucknorris.io/jokes/random?category={scelta}')  
    r = r.json()
    print(r["value"])

elif int(scelta) == 2:
    scelta = input("inserire una parola da cercare: ")
    r = requests.get(f"https://api.chucknorris.io/jokes/search?query={scelta}")  
    r = r.json()
    r = r["result"]
    if r == []:
        print("parola non trovata in nessuna frase")
    else:
        for risultato in r:
            print(f"{risultato['value']}\n")