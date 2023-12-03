# poke_calculator
Esse projeto visa utilizar dos métodos de data visualization, programação em python, automação e de interfaces gráficas.
##

  A parte lógica do calculador em questão, presente em [code.py](https://github.com/estevao-luiz/poke_calculator/blob/main/code.py), é uma implementação de um sistema para avaliar a compatibilidade da equipe de Pokémon do jogador com a região do jogo. Ele realiza as seguintes etapas:
  
1. Localização da Região e Bioma:

&nbsp;&nbsp;&nbsp;&nbsp;Determina a região, área e bioma do jogador com base em inputs ou informações fixas.

2. Análise de Encontros:

&nbsp;&nbsp;&nbsp;&nbsp;Utiliza informações de encontros em um arquivo para calcular a probabilidade de encontrar diferentes tipos de Pokémon na região 
&nbsp;&nbsp;&nbsp;&nbsp;específica.

3. Cálculo de Taxas:

&nbsp;&nbsp;&nbsp;&nbsp;Calcula as taxas de encontro para cada Pokémon com base em sua presença na região.

4. Análise de Tipos:

&nbsp;&nbsp;&nbsp;&nbsp;Obtém os tipos dos Pokémon mais prováveis de serem encontrados na região.

5. Sugestão de Equipe Ideal:

&nbsp;&nbsp;&nbsp;&nbsp;Sugere uma equipe ideal de 6 Pokémon com base nos tipos mais eficazes para a região.

6. Comparação de Equipes:

&nbsp;&nbsp;&nbsp;&nbsp;Compara a equipe atual do jogador com a equipe ideal sugerida, fazendo ajustes se necessário.

&nbsp;O código utiliza arquivos externos para obter informações sobre Pokémon e taxas de encontro, além de incluir visualizações de dados através de gráficos. A modularidade e estrutura do código facilitam a compreensão e manutenção do sistema. 

##

&nbsp;Com relação à visualização dos dados, temos o script [data_visual](https://github.com/estevao-luiz/poke_calculator/blob/main/data_visual.py) o qual é importado em code.py como módulo. Tratando-se de uma implementação utilizando a biblioteca Matplotlib e outras para a visualização de dados relacionados aos tipos de Pokémon. 

&nbsp;O script começa definindo uma lista vazia chamada tipos_pokemon. Em seguida, há uma função chamada main, que realiza as seguintes tarefas:

* Conta a ocorrência de cada tipo de Pokémon na lista tipos_pokemon.

* Extrai os dados necessários para criar um gráfico de barras, incluindo tipos e quantidades.

* Associa cores a cada tipo de Pokémon com base em um dicionário predefinido.

* Cria um gráfico de pizza que mostra a distribuição de tipos de Pokémon na região.

Além disso, o código define duas funções adicionais:

* plot_encounter_rate: Plota um gráfico de barras mostrando a taxa de encontro de diferentes Pokémon, usando nomes e taxas fornecidos como parâmetros.

* plot_encounter_heatmap: Cria mapas de calor para correlações entre efetividade e resistência dos tipos de Pokémon, utilizando DataFrames do Pandas e paletas de cores específicas.

Finalmente, a função main(tipos_pokemon) é chamada, esperando valores da lista tipos_pokémon que vêm de code.py.

## 

&nbsp;&nbsp;&nbsp;&nbsp;A partir disso, temos o script [interactive_map.py](https://github.com/estevao-luiz/poke_calculator/blob/main/interactive_map.py) que utiliza a biblioteca Tkinter para criar interfaces gráficas e a biblioteca Matplotlib para gerar mapas interativos. Em resumo, o script se descreve com as seguintes classes e suas respectivas funcionalidades:

* Classe  **InteractiveButton_version**:

Cria uma janela gráfica com um mapa de regiões.
As regiões são polígonos interativos em que o usuário pode clicar.
Ao clicar em uma região, a classe captura a versão clicada, retorna o valor de *version* e fecha a janela.

* Classe **InteractiveMap_paldea**:

Similar à classe InteractiveButton_version, mas para um mapa diferente.
Permite ao usuário selecionar uma província, escolhendo o valor de *province* clicando em um polígono correspondente.

* Classe **InteractiveMap_province**:

Semelhante às anteriores, mas para áreas dentro de uma província.
O usuário pode clicar em uma área e a classe captura a área selecionada, devolvendo o valor de *area*.

* Classe **InteractiveButton_biome**:

Exibe um mapa com diferentes biomas representados por polígonos interativos.
O usuário pode clicar em um bioma dentro de uma área e a classe captura o bioma selecionado (*biome*), verificando se o bioma pertence à área e província previamente selecionadas.

* Função **main**:

Define coordenadas para diferentes regiões em uma variante.
Cria uma instância da classe **InteractiveButton_version** para permitir ao usuário escolher uma variante.
Com base na variante escolhida, cria uma instância da classe **InteractiveMap_paldea** para permitir ao usuário escolher uma província.
Com base na província escolhida, cria uma instância da classe **InteractiveMap_province** para permitir ao usuário escolher uma área.
Finalmente, com base na área escolhida, cria uma instância da classe **InteractiveButton_biome** para permitir ao usuário escolher um bioma.


&nbsp;&nbsp;&nbsp;&nbsp;Em suma, o código utiliza a biblioteca Matplotlib para exibir os mapas e a biblioteca Shapely para verificar se um ponto (clicado pelo usuário) está dentro de um polígono. Ressaltando que todos os dicionários contendo os pontos dos polígonos foram obtidos no site do VGG Image Anotator. As informações capturadas durante as interações do usuário são armazenadas nas variáveis *version*, *province*, *area*, e *biome*. O script fornece uma interface gráfica para exploração de diferentes regiões, províncias, áreas e biomas em um mapa. Os dados captados são retornados para a execução da lógica de calculadora de code.py.

##

&nbsp;&nbsp;&nbsp;&nbsp;Por fim, temos [exe.py](https://github.com/estevao-luiz/poke_calculator/blob/main/exe.py) que une a execução de todos os outros scripts. Sua estrutura funciona da seguinte forma: 

* Interface Gráfica:

Utiliza a biblioteca Tkinter para criar uma janela principal.
A janela contém campos para inserção de informações da equipe de Pokémon desejada.
Um botão "Submit" inicia a análise da equipe.

* Funcionalidade Principal (main):

Recebe as informações inseridas e a equipe desejada.
Utiliza um módulo chamado **code** para realizar várias operações, como encontrar Pokémon na área, avaliar encontros, calcular taxas, avaliar tipos, calcular danos e determinar a equipe ideal.
Compara a equipe inserida pelo usuário com a equipe ideal.

* Apresentação de Resultados:

Após a análise, finalmente, exibe uma caixa de mensagem com o resultado da comparação entre a equipe do usuário e a equipe ideal.

##

&nbsp;&nbsp;&nbsp;&nbsp;Em conclusão, o usuário vai receber a equipe ideal para certa região, selecionada por ele previamente de forma interativa. Além de poder avaliar a distribuição dos dados, através do ferramental de visualização disponibilizado.


