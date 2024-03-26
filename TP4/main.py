import sys
import ply.lex as lex





class Main():

    def __init__(self):
        self.data = []

    def parser(self):
        self.data = sys.stdin.readlines()



reservedWords = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',
    'inner': 'INNER',
    'outer': 'OUTER',
    'like': 'LIKE',
    'full': 'FULL',
    'left': 'LEFT',
    'right': 'RIGHT',
    'on': 'ON',
    'join': 'JOIN',
    'group': 'GROUP',
    'by': 'BY',
    'having': 'HAVING',
    'union': 'UNION',
    'order': 'ORDER',
    'limit': 'LIMIT',
    'as': 'AS',
}

tokens = [
    'IDENTIFIER',
    'VARIABLE',
    'TYPO',
    'EVERYTHING',
    'COMMA',
    'NUMBER',
    'PERIOD',
    'OPERATOR',
    'LPAREN',
    'RPAREN',
    'SEMICOLON'
] + list(reservedWords.values())

t_COMMA = r'\,'
t_EVERYTHING = r'\*'
t_NUMBER = r'\d+'
t_PERIOD = r'\.'
t_OPERATOR = r'[+\-/=<>]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r'\;'
t_ignore  = ' \t'

def t_IDENTIFIER(t):
    r'[A-Z_][A-Z_0-9]*'
    t.type = reservedWords.get(t.value.lower(), 'TYPO')
    return t

def t_VARIABLE(t):
    r'[a-z_][a-z_0-9]*'
    t.type = 'VARIABLE' if not reservedWords.get(t.value.lower()) else 'TYPO'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caractere '%s' ilegal na posição %d" % (t.value[0], t.lexpos))
    t.lexer.skip(1)



if __name__ == "__main__":
    main = Main()
    main.parser()

    lexer=lex.lex()
    for line in main.data:
        lexer.input(line)

        for token in lexer:
            print(token)
        
        print("\n _______________ \n")
    