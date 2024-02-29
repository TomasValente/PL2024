import sys
import re




class Main():

    def __init__(self):

        self.data = []
        self.sum = 0
        self.switch = True #True == ON | FALSE == OFF


    def parser(self):
        self.data = sys.stdin.readlines()


    def sumSeq(self):
        on = '[Oo][Nn]'
        off = '[Oo][Ff][Ff]'
        num = '\d+'
        result = '='

        i = 1

        for line in self.data:
            syntax = f"(?P<on>{on})|(?P<off>{off})|(?P<num>{num})|(?P<result>{result})"

            catches = re.finditer(syntax, line)

            for catch in catches:
                if catch.lastgroup == 'result':
                    print(f"Resultado da {i}ª sequência: {self.sum}\n")
                    i += 1

                elif catch.lastgroup == 'on':
                    self.switch = True
                    print(f"Switch ON!\n")

                elif catch.lastgroup == 'off':
                    self.switch = False
                    print(f"Switch OFF!")
                    print(f"Soma total até ao momento: {self.sum}\n")

                elif catch.lastgroup == 'num' and self.switch:
                    self.sum += int(catch.group('num'))

        print(f"Somador terminado. Foram somadas {i-1} sequências.\n")
    



if __name__ == "__main__":
    main = Main()
    main.parser()
    main.sumSeq()