# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    #escrever seu nome no lugar de Alex e sua idade no lugar de 12
    nome = "Alex" # escreva seu nome
    idade = "12" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def father():

    #escrever o nome de seu pai no lugar de VITOR e a idade no lugar de 40
    nome = "Vítor" # escreva seu nome
    idade = "40" # escreva sua idade

    return render_template('pai.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.route("/mae")
def mother():

    #escrever o nome de sua mãe no lugar de Erica e a idade no lugar de 37
    nome = "Erica" # escreva seu nome
    idade = "37" # escreva sua idade

    return render_template('mae.html' , nome = nome , idade = idade)


# defina a rota para a página do amigo
@app.route("/amigo")
def friend():

    #escrever o nome de seu amigo no lugar de Pedro e a idade no lugar de 12
    nome = "Pedro" # escreva seu nome
    idade = "12" # escreva sua idade

    return render_template('amigo.html' , nome = nome , idade = idade)


# adicione outras rotas, se você quiser


# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
