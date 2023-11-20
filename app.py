from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registrar_cliente', methods=['GET', 'POST'])
def registrar_cliente():
    dados = {}
    
    if request.method == 'POST':
        dados['Usuário'] = request.form.get('usuario')
        dados['Nome'] = request.form.get('nome')
        dados['Gênero'] = request.form.get('genero')
        dados['Endereço'] = request.form.get('endereco')
        dados['Data de Nascimento'] = request.form.get('data_nascimento')


    return render_template('registrar_cliente.html', dados=dados)

@app.route('/registrar_produto', methods=['GET', 'POST'])
def registrar_produto():
    dados_produto = {}
    
    if request.method == 'POST':
        dados_produto['Nome do Produto'] = request.form.get('nomeProduto')
        dados_produto['Preço'] = request.form.get('preco')
        dados_produto['Data de Cadastro'] = request.form.get('data_cadastro')

    return render_template('registrar_produto.html', dados_produto=dados_produto)

if __name__ == '__main__':
    app.run(debug=True)