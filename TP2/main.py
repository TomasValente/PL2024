import re
import sys



sys.stdout = open('output.html', 'w')

class Main():
    def __init__(self):

        self.data = []
        self.ordered_list = False


    def parser(self):
        self.data = sys.stdin.readlines()


    def markdown_to_html(self):
        try:

            for line in self.data:

                #Lista ordenada
                if re.match(r'^\d+\.', line):
                    if not self.ordered_list:
                        print('<ol>')
                        self.ordered_list = True
                    line = re.sub(r'^\d+\. (.*)$', r'<li>\1</li>', line)
                else:
                    if self.ordered_list:
                        print('</ol>')
                        self.ordered_list = False
                
                # Cabeçalhos
                line = re.sub(r'^# (.*)$', r'<h1>\1</h1>', line)
                line = re.sub(r'^## (.*)$', r'<h2>\1</h2>', line)
                line = re.sub(r'^### (.*)$', r'<h3>\1</h3>', line)

                # Bold
                line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)

                # Itálico
                line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)

                # Lista sem ordem
                line = re.sub(r'^- (.*)$', r'<li>\1</li>', line)

                # Blockquote
                line = re.sub(r'^> (.*)$', r'<blockquote>\1</blockquote>', line)

                # Código
                line = re.sub(r'`(.*?)`', r'<code>\1</code>', line)

                # Imagem
                line = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', line)

                # Link
                line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)

                # Barra horizontal
                line = re.sub(r'^---$', r'<hr>', line)

                print(line.strip())

            if self.ordered_list:
                print('</ol>')

        except Exception as e:
            print(e)



if __name__ == "__main__":
    main = Main()
    main.parser()
    main.markdown_to_html()