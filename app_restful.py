from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

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


class Home(Resource):
	
	def get(self, id):
	
		try:
			for cadastro in tarefas:
				if cadastro["id"] == id:
					return jsonify(cadastro)
			# Caso ID não exista.
			response = {"status":"Erro", "mensagem":f"Usuário de ID {id} inexistente."}
		except:
			response = {"status":"Erro", "mensagem": "Erro desconhecido."}
		return jsonify(response)


	def put(self, id):
	
		try:
			for cadastro in tarefas:
				if cadastro["id"] == id:
					dados = json.loads(request.data)
					idx = tarefas.index(cadastro)
					tarefas[idx]["status"] = dados["status"]
					return jsonify(cadastro)
		except:
			jsonify({"status":"Erro", "mensagem": "Erro desconhecido."})
			
		
	def delete(self, id):
	
		try:
			for cadastro in tarefas:
				if cadastro["id"] == id:

					tarefas.remove(cadastro)
					return jsonify({"status": "Sucesso", "mensagem": "Registro removido com sucesso."})
		except:
			jsonify({"status":"Erro", "mensagem": "Erro desconhecido."})
			
			
class ListarTarefas(Resource):

	def get(self):
		return jsonify(tarefas)
		
	def post(self):
		dados = json.loads(request.data)
		tarefas.append(dados)
		return jsonify(tarefas)
			
			
api.add_resource(Home, "/tarefas/<int:id>")
api.add_resource(ListarTarefas, "/tarefas/")

if __name__ == '__main__':
	app.run(debug=True)