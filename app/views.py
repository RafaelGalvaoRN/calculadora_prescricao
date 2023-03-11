from app import app
from flask import render_template, request
from app.util import *

@app.route('/')
def index():
    return render_template("public/index.html")


@app.route('/faq')
def faq():
    return render_template("public/faq.html")


@app.route('/contato')
def contato():
    return render_template("public/contato.html")


@app.route('/documentacao')
def documentacao():
    return render_template("public/documentacao.html")


@app.route('/prescricao', methods=["GET", "POST"])
def prescricao():
    if request.method == "GET":
        legislacao = ['Código Penal', 'Lei Maria da Penha', 'Lei de Drogas', 'Lei 9.099 / 95', 'Lei de Lavagem']

        return render_template('public/prescricao.html', legislacao=legislacao)

    elif request.method == "POST":
        dados_prescricao = {
            'processo': request.form['processo'],
            'reu': request.form['reu'],
            'data_fato': request.form['data_fato'],
            'legislacao': request.form['legislacao'],
            'crime': request.form['crime'],
            'recebimento_denuncia_bool': request.form['recebimento_denuncia_bool'],
            'Dt_Denuncia': request.form['Dt_Denuncia'],
            'suspensao_prescricao_bool': request.form['suspensao_prescricao_bool'],
            'Dt_inicio_suspensao': request.form['Dt_inicio_suspensao'],
            'Dt_fim_suspensao': request.form['Dt_fim_suspensao']
        }

        print(dados_prescricao)

        resultado, parecer = analisa_prescricao(dados_prescricao)

        # tipo_penal = ['Ameaca', "Roubo", "Furto", "Lesao", "Homicídio"]

        # return render_template('prescricao.html', legislacao=legislacao, tipo_penal=tipo_penal)
        print(dados_prescricao)
        print(resultado)
        print('aqui')
        print(resultado['resultado'])
        print(parecer)
        return render_template('public/prescricao_resultado.html', dados_prescricao=dados_prescricao, resultado=resultado,
                               parecer=parecer, corrige_ordem_da_data_str=corrige_ordem_da_data_str)
