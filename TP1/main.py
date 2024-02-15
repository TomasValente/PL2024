import sys
from format import *



sys.stdout = open('output.txt', 'w')

class Main():

    def __init__(self):

        self.data = []

        self.escaloes = [0] * 20
        self.modList = []
        self.nAptos = 0
        self.nInaptos = 0
        self.nTotal = 0



    def calcular_escalao_etario(self, idade):
        return idade // 5

    def parser(self):

        self.data = sys.stdin.readlines()
        self.data.pop(0)
        
        for line in self.data:
            dados = line.strip().split(',')
            modalidade = dados[8]

            if modalidade not in self.modList:
                self.modList.append(modalidade)

            if dados[12] == 'true':
                self.nAptos += 1

            else:
                self.nInaptos += 1

            pos = self.calcular_escalao_etario(int(dados[5]))
            self.escaloes[pos] += 1
        
        self.nTotal = self.nAptos + self.nInaptos
  


if __name__ == "__main__":
    main = Main()
    main.parser()

    formatter = Format(main.data, main.escaloes, main.modList, main.nAptos, main.nInaptos, main.nTotal)
    formatter.format_modlist()
    formatter.format_percentage()
    formatter.format_escalao()
        