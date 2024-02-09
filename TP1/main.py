import sys
from format import *

sys.stdin = open('emd.csv', 'r')
sys.stdout = open('output.txt', 'w')



class Main():

    def __init__(self):

        self.data = sys.stdin.readlines()
        self.data.pop(0)

        self.modList = []
        self.nAptos = 0
        self.nInaptos = 0
        self.nTotal = 0



    def parser(self):
        
        for line in self.data:
            dados = line.strip().split(',')
            modalidade = dados[8]

            if modalidade not in self.modList:
                self.modList.append(modalidade)

            if dados[12] == 'true':
                self.nAptos += 1

            else:
                self.nInaptos += 1
        
        self.nTotal = self.nAptos + self.nInaptos
  


if __name__ == "__main__":
    main = Main()
    main.parser()

    formatter = Format(main.data, main.modList, main.nAptos, main.nInaptos, main.nTotal)
    formatter.format_modlist()
    formatter.format_percentage()
    formatter.format_escalao()
        