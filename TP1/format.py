



class Format():

    def __init__(self, data, modList, nApdtos, nInaptos, nTotal):

        self.data = data

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
        perAptos = round(perAptos, 1)
        perInaptos = (self.nInaptos / self.nTotal) * 100
        perInaptos = round(perInaptos, 1)

        print("┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐")
        print("|                                                               |")
        print(f"| Percentagem de atletas aptos para prática desportiva: {perAptos}%   |")
        print(f"| Percentagem de atletas inaptos para prática desportiva: {perInaptos}% |")
        print("|                                                               |")
        print("└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\n\n")

    

    def format_escalao(self):
        #print(self.data)
        pass
