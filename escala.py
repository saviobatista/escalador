# coding=UTF-8
from datetime import time
#Script gerador de escala, deve gerar uma escala para N empregados com variaveis de relevancia com prioridades e turnos
#1. Os turnos, deve ter nome, hora de inicio, duração.
#2. Uma variável com número de dias de folga entre as sequencias de escala
#3. Objeto empregado tem propriedades de relevancia e agrupamento

class Escala:
    def __init__(self, folga, turnos, empregados):
        self.folga = folga
        self.turnos = turnos
        self.empregados = empregados
    def gerar(self, inicio):
        self.inicio = inicio
        self.equipes = [ ]
        #Define equipes
        for i in range(len(self.turnos) + self.folga):
            self.equipes.append(Equipe())
        #Define as equipes por empregados
        #Para isto, vou reordenar a lista de empregados segundo a prioridade: Encarregado > Substituto > Instrutor > Tempo > Ingles
        self.empregados.sort(key=Empregado.prioridade)
        print("Empregados em ordem: ")
        for empregado in self.empregados:
            print(str(empregado))

        for idx, empregado in enumerate(self.empregados):
            key = idx%len(self.equipes)
            print(str(key)+empregado.nome)
            self.equipes[key].addEmpregado(empregado)
        
        for equipe in self.equipes:
            print(str(equipe))
    

class Equipe:
    seq = 0
    objects = []
    empregados = []
    def __init__(self):
        self.id = self.__class__.seq
        self.__class__.seq += 1
        self.__class__.objects.append(self)
    def addEmpregado(self,empregado):
        print(self.empregados)
        self.empregados.append(empregado)
    def getNome(self):
        nomes = ['Azul','Verde','Vermelho','Branco','Lilás','Laranja','Cinza','Violeta']
        return nomes[self.id]
    def __str__(self):
        ret = "\n - EQUIPE "+self.getNome()+"\n\n"
        for empregado in self.empregados:
            ret += "    + " + empregado.nome
        return ret

class Turno:
    def __init__(self, nome, inicio, duracao, minimo):
        self.nome = nome
        self.inicio = inicio
        self.duracao = duracao
        self.minimo = minimo

class Empregado:
    valor = 0.0
    usarIngles = 0
    def __init__(self, nome, encarregado, substituto, instrutor, tempo, ingles):
        self.nome = nome
        self.encarregado = encarregado
        self.substituto = substituto
        self.instrutor = instrutor
        self.tempo = tempo
        self.ingles = ingles
    def __str__(self):
        return self.nome + " - " + str(self.valor)
    def prioridade(empregado):
        #Esta função define um valor de força para um empregado definindo a distribuição do mesmo
        valor = 0.0
        if empregado.encarregado == 1:
            valor += 8.0
        if empregado.substituto == 1:
            valor += 4.0
        if empregado.instrutor == 1:
            valor += 2.0
        valor += empregado.tempo/35.0 # O máximo possível de anos de trabalho é 35 anos, daria fator 1
        valor += empregado.ingles/6.0 # O máximo possível é nível 6, daria fator 1
        empregado.valor = valor
        return valor * -1.0
    @classmethod
    def all(cls):
        return cls.objects

folga=3 #dias de folga
turnos=[ Turno('A','07:00',8,4), Turno('B','15:00',8,4), Turno('C','23:00',8,3) ]
empregados=[
    Empregado('A',1,0,1,20,4),
    Empregado('B',1,0,1,7,4),
    Empregado('C',1,0,1,20,5),
    Empregado('D',1,0,0,15,4),
    Empregado('E',1,0,1,25,4),
    Empregado('F',0,1,1,8,4),
    Empregado('G',0,1,0,25,6),
    Empregado('H',0,1,0,15,4),
    Empregado('I',0,1,1,5,5),
    Empregado('J',0,1,0,15,5),
    Empregado('K',1,1,1,10,5),
    Empregado('L',0,0,0,3,4)
]
escala=Escala(folga,turnos,empregados)
escala.gerar('2021-02-28')
