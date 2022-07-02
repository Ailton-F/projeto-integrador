from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', defaults={'type': 1})
@app.route('/login/{type}')
def login(type):
    if type == 1:
      return render_template('login/login.html')

@app.route('/cadastro', defaults={'id': 1})
@app.route('/cadastro/<id>')
def cadastro(id):
  if id == '2' or id == 2:
    return render_template('cadastro/cadastro_instituicao.html')
  elif id == '3' or id == 3:
    return render_template('cadastro/cadastro_profissional.html')
  elif id == '4' or id == 4:
    return render_template('cadastro/cadastro_asilo.html')
  else:
    return render_template('cadastro/cadastro_pessoa.html')

@app.route('/informacoes')
def informacoes():
  asilos = [{"nome": "Bom Idoso"},{"nome": "Paraíso da meia idade"},{"nome": "Idosos com Cristo"},{"nome": "Asilo Padre João"},{"nome": "Asilo de Nossa Senhora da Conceição"}]
  return render_template('informacoes.html', asilos=asilos)

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

@app.route('/doacoes')
def doacoes():
    return render_template('doacoes.html')


app.run(host='0.0.0.0', port=81)
