import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configurar aplicação
app = Flask(__name__)

# Assegurar que os modelos sejam auto-recarregados
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configurar a biblioteca do CS50 para usar o banco de dados SQLite
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Adicionar a entrada do usuário no banco de dados
        nome = request.form.get("nome")
        mes = request.form.get("mes")
        dia = request.form.get("dia")
        
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?,?,?)", nome, mes, dia)
        return redirect("/")

    else:
        # TODO: exibir as entradas no banco de dados em index.html
        
       database = db.execute("SELECT * FROM birthdays") 
       return render_template("index.html", database=database)  


