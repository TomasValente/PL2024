# PL2024-TPC1

## Aluno

- **Nome:** João Tomás Gonçalves de Sousa Carneiro Valente
- **Número:** A100540

## Objetivos
- **Ler o dataset, processá-lo e criar os seguintes resultados:**
    - **1-** Listar por ordem alfabética das modalidades desportivas;
    - **2-** Apresentar as percentagens de atletas aptos e inaptos para a prática desportiva;
    - **3-** Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

**Nota:** É proibido usar o módulo CSV.

## Compilação
- **Input:** *python3 main.py < emd.csv*
- **Output:** É criado um ficheiro "*output.txt*", correspondente ao *stdout* de modo a apresentar os resultados obtidos.



## Resolução do problema
- **Módulos:**
    - **main.py:** Módulo responsável por fazer o *parser* do conteúdo do *CSV*, armazenar o mesmo e executar as funções necessárias para gerar o *output*.
    - **format.py:** Módulo responsável pela formatação do *output* assim como pequenos cálculos necessários para a resolução do problema.