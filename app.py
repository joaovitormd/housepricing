#Construir API
from flask import Flask, request
from datetime import datetime
import joblib
import sqlite3

#Instanciar o app
app = Flask(__name__)

#Carregar o modelo
model = joblib.load('modelo_randomforest_v100.pkl')

#Criar conexão com o banco de dados
conexao_banco = sqlite3.connect('banco_de_dados_API.db')
cursor = conexao_banco.cursor()

#função para receber a API
@app.route('/API_preditivo/<area>;<quartos>;<banheiro>;<vagas_garagem>;<andar>;<animal>;<mobilhado>;<condominio>;<iptu>', methods=['GET'])
def funcao_01(area, quartos, banheiro, vagas_garagem, andar, animal, mobilhado, condominio, iptu):

    #Data e hora do inicio da execução
    data_inicio = datetime.now()

    lista_parametros = [
                            float(area), float(quartos), float(banheiro), float(vagas_garagem), 
                            float(andar), float(animal), float(mobilhado), float(condominio), float(iptu)
                        ]

    try:
        #Previsao
        previsao = model.predict([lista_parametros])

        #Inserir o valor da previsao na lista
        lista_parametros.append(str(previsao))

        #Concatenando a lista
        input=''
        for valor in lista_parametros:
            input = input + ';' + str(valor)

        #Data e hora do termino da execução
        data_fim = datetime.now()

        #Calcular o tempo de processamento
        processamento = data_fim - data_inicio

        #Criar conexão com o banco de dados
        conexao_banco = sqlite3.connect('banco_de_dados_API.db')
        cursor = conexao_banco.cursor()

        #query
        query_inserir_dados = f'''
            INSERT INTO Log_API (inputs, inicio, fim, processamento)
            VALUES ('{input}', '{data_inicio}', '{data_fim}', '{processamento}')

        '''

        #Executar a query
        cursor.execute(query_inserir_dados)
        conexao_banco.commit()

        #Fechar a conexão com o banco de dados
        cursor.close()

        #Retonar o valor da previsao
        return{'valor_aluguel': str(previsao)}

    except:
        return {'Aviso': 'Aconteceu algum erro'}

if __name__ == '__main__':
    app.run(debug=True)