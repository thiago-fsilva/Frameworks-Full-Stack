from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def home():
    lista = [
        {
        "tipo" :"Séries"
        ,"imagem" :"../static/img/Supernatural.jpg"
        },
        {
            "tipo": "Filmes"
            , "imagem": "../static/img/harrypotter3.jpg"
        },
        {
            "tipo": "Animes"
            , "imagem": "../static/img/dragon-ball.jpg"
        }
        ]
    Imagens = ['Supernatural','harrypotter3','dragon-ball']
    return render_template('index.html', nomeSite='TVFlix', conteudo=lista)

if __name__ == '__main__':
    app.run(debug=True)