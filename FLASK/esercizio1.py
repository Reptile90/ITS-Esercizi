from flask import Flask,url_for

app = Flask(__name__)

@app.route('/about')
def show_description()->str:
    return '<h3>NUOVA APP CON FLASK</h3>'


@app.route('/user/<string:nome>')
def welcome(nome)->str:
    return f"<h3>Benvenuto {nome}!</h3>"


@app.route('/square/<int:n>')
def square(n)->int:
    sqr = n**2
    return f"<h3>Il quadrato del numero scelto è {sqr}</h3>"

@app.route('/sum/<int:a>/<int:b>')
def somma(a:int,b:int)->int:
    somma = a+b
    return f"<h3>La somma dei due numeri è {somma}</h3>"

@app.route('/')
def home():
    homepage = f"""
        <h1>Homepage</h1>
        <ul>
            <li><a href="{url_for('show_description')}">Vai alla pagina About</a></li>
            <li><a href="{url_for('welcome', nome='Stefano')}">Profilo di Stefano</a></li>
            <li><a href="{url_for('square', n=7)}">Quadrato di 7</a></li>
            <li><a href="{url_for('somma', a=5, b=3)}">Somma di 5 + 3</a></li>
            <li><a href="{url_for('elenco_post')}">POSTS</a></li>

        </ul>
        """
    return homepage

@app.route('/utenti')
def lista_utenti():
    utenti = ['Stefano', 'Lorenzo', 'Marcel', 'Cristiano', 'Dario']
    html = "<h2>Elenco utenti</h2><ul>"
    for nome in utenti:
        link = url_for('welcome', nome = nome)
        html += f'<li><a href="{link}">{nome}</a></li>'
    html += "</ul>"
    return html


posts = {
    1: "Come usare Flask per creare web app",
    2: "Introduzione a Python per principianti",
    3: "Gestione delle route dinamiche con url_for",
    4: "Creare template HTML con Jinja2",
    5: "Deploy di un'app Flask su Heroku"
}
@app.route('/post/<int:id>')
def mostra_post(id):
    titolo = posts.get(id, "Articolo non trovato")
    return f"<h2>Post #{id}</h2><p>{titolo}</p>"

@app.route('/posts')
def elenco_post():
    html = "<h1>Elenco articoli</h1><ul>"
    for id, titolo in posts.items():
        link = url_for('mostra_post', id=id)
        html += f'<li><a href="{link}">{titolo}</a></li>'
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5500)
