class Carro:
    def _init_(self, marca, modelo, cor, combustivel, ano, id = None):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.ano = ano

class Usuario:
    def _init_(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha