from flask import Flask, render_template, redirect, url_for, request, make_response
from datetime import date, datetime
from re import U
import sqlite3
import string
import random
#import AlphaBot

app = Flask(__name__)

token = ""
for _ in range(10):
    token += random.choice(string.ascii_letters)

def validate(username, password):
    completion = False
    con = sqlite3.connect('./db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS")
    rows = cur.fetchall()
    for row in rows:
        dbUser = row[0]
        dbPass = row[1]
        if dbUser==username:
            completion=check_password(dbPass, password)
    con.close()
    return completion

def check_password(hashed_password, user_password):
    return hashed_password == user_password

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    cookie = request.cookies.get('username')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            con = sqlite3.connect('./db.db')
            cur = con.cursor()
            cur.execute(f"INSERT INTO login (id_utente, data, ora, username, cookie) VALUES ('{token}', '{date.today()}', '{datetime.now()}', '{username}', '{cookie}');")
            con.commit()
            return redirect(url_for('main'))
    if cookie == None:
        resp  = make_response(render_template('login.html', error=error))
        resp.set_cookie('username', 'nuovoutente')
    return render_template('login.html', error=error)

@app.route(f'/{token}', methods =['GET', 'POST'])
def main():
    #bot = AlphaBot.AlphaBot()  
    if request.method == 'POST':
        con = sqlite3.connect('./db.db')
        cur = con.cursor()
        cont = -1

        if request.form.get('commands') == 'w':
            comando = cur.execute('SELECT sequenza FROM comandi where comandi.comando = "w"').fetchall()
            comando = comando[0][0]
            lista_comandi = comando.split(",")
            print("avanti")
            
        elif request.form.get('commands') == 's':
            comando = cur.execute('SELECT sequenza FROM comandi where comandi.comando = "s"').fetchall()
            comando = comando[0][0]
            lista_comandi = comando.split(",")
            print("indietro")
            
        elif request.form.get('commands') == 'd':
            comando = cur.execute('SELECT sequenza FROM comandi where comandi.comando = "d"').fetchall()
            comando = comando[0][0]
            lista_comandi = comando.split(",")
            print("destra")
            
        elif request.form.get('commands') == 'a':
            comando = cur.execute('SELECT sequenza FROM comandi where comandi.comando = "a"').fetchall()
            comando = comando[0][0]
            lista_comandi = comando.split(",")
            print("sinistra")

        elif request.form.get('commands') == 'text':
            testo = ""
            if testo == "":
                comando = cur.execute(f'SELECT sequenza FROM comandi where comandi.comando = "{testo}"').fetchall()
                comando = comando[0][0]
                lista_comandi = comando.split(",")  
            else:
                print("errore")

        for comando in lista_comandi:                                 #lista comandi contiene tutti i comandi e i tempi, la si scorre prendendo ogni comando e tempo e eseguendolo singolarmente
            cont += 1
            if comando == "w":
                bot.time_forward(lista_comandi[cont+1])               #cont+1 serve a prendere il tempo del relativo comando
                print("avanti")                                       #in quanto il tempo relativo al comando si trova alla posizione successiva
            if comando.lower() == "s":
                bot.time_backward(lista_comandi[cont+1])
                print("indietro")
            if comando.lower() == "d":
                bot.time_right(lista_comandi[cont+1])
                print("destra")
            if comando.lower() == "a":
                bot.time_left(lista_comandi[cont+1])
                print("sinistra")
        con.close()
    return render_template('index.html')


if __name__== "__main__":
    app.run(debug=True, host='localhost') #, host='192.168.0.129'