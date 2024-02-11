



class Format():

    def __init__(self, data, escaloes, modList, nApdtos, nInaptos, nTotal):

        self.data = data

        self.escaloes = escaloes
        self.modList = modList
        self.nAptos = nApdtos
        self.nInaptos = nInaptos
        self.nTotal = nTotal

    

    def format_modlist(self):
        self.modList = sorted(self.modList)
        modByLetter = {}

        print("┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")
        print("|   Lista de Modalidades Praticadas:   |\n")

        for mod in self.modList:
            letter = mod[0].upper()

            if letter not in modByLetter:
                modByLetter[letter] = []

            modByLetter[letter].append(mod)
        
        for letter, mods in modByLetter.items():
            print(f"{letter}")
            for mod in mods:
                print(f"{mod}")
            print('\n')

        print("|                                      |")
        print("└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n\n")



    def format_percentage(self):
        perAptos = (self.nAptos / self.nTotal) * 100
        perInaptos = (self.nInaptos / self.nTotal) * 100

        print("┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")
        print("|                                                                 |")
        print(f"| Percentagem de atletas aptos para prática desportiva = {perAptos:.2f}%   |")
        print(f"| Percentagem de atletas inaptos para prática desportiva = {perInaptos:.2f}% |")
        print("|                                                                 |")
        print("└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n\n")

    

    def format_escalao(self):
        idade = 0

        print("Percentagem por escalão etário: \n")
        for escalao in self.escaloes:
            if escalao != 0:
                print(f'{idade}-{idade+4} = {(escalao / self.nTotal) * 100:.2f}%\n')
            idade += 5
