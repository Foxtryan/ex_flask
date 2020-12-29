from flask import Flask, request, jsonify
import json
import requests


app = Flask(__name__)


tarefas = [
	{
		"id": 1,
		"tarefa": "Comprar Almoço",
		"responsavel": "Douglas",
		"status": "Pendente",
	},
	{
		"id": 2,
		"tarefa": "Ganhar na Loto",
		"responsavel": "Destino",
		"status": "Pendente",
	},
	{
		"id": 3,
		"tarefa": "Estudar",
		"responsavel": "Rafael",
		"status": "Em andamento",
	}	
]

# GET retorna tudo, POST cria novo registro
# POST o ID esta sendo passado manualmente, por fins de estudo
@app.route("/tarefas/", methods=["GET", "POST"])
def home():
	if request.method == "GET":
		return jsonify(tarefas)
	elif request.method == "POST":
		dados = json.loads(request.data)
		tarefas.append(dados)
		return jsonify(tarefas)


# GET retorna somente o arquivo ID, PUT altera a ID
@app.route("/tarefas/<int:id>", methods=["GET", "PUT", "DELETE"])
def teste(id):

	for cadastro in tarefas:
		if cadastro["id"] == id and request.method == "GET":
			return jsonify(cadastro)
		
		# MULTIPLAS ALTERACOES EM UMA TAREFA ENQUANTO DENTRO DO LOOP CAUSA FALHAS
		# COMO EH MATERIAL DE ESTUDO, ONDE UMA ALTERACAO SERA REALIZADA POR VEZ
		# MANTIVE ASSIM
		elif cadastro["id"] == id and request.method == "PUT":
			dados = json.loads(request.data)
			idx = tarefas.index(cadastro)
			print("DADOS:", dados)
			tarefas[idx]["status"] = dados["status"]
			return jsonify(cadastro)
			
		elif cadastro["id"] == id and request.method == "DELETE":
			#dados = json.loads(request.data)
			#idx = tarefas.index(cadastro)
			tarefas.remove(cadastro)
			return jsonify({"mensagem": "Registro apagado com sucesso"})
			
	return jsonify({"mensagem": "Registro não encontrado"})
	
	
if __name__ == '__main__':
	app.run(debug=True)
