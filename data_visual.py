import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import Counter
import numpy as np
import seaborn as sns
import pandas as pd



#tipos_pokemon = ['Normal, ', 'Fighting, ', 'Flying, ', 'Poison, ', 'Ground, ', 'Rock, ', 'Bug, ', 'Ghost, ', 'Steel, ', 'Fire, ', 'Water, ', 'Grass, ', 'Electric, ', 'Psychic, ', 'Ice, ', 'Dragon, ', 'Dark, ', 'Fairy, ']
tipos_pokemon = []

def main(tipos_pokemon):
    
    #print(tipos_pokemon)
    
    # Contador de tipos de Pokémon
    contador_tipos = Counter(tipos_pokemon)
    
    # Extrair dados para o gráfico de barras
    tipos = list(contador_tipos.keys())
    quantidades = list(contador_tipos.values())
    
    #Dicionário que associa cada tipo a uma cor
    cores_pokemon = {
    'Normal': 'lightgrey',
    'Fighting': 'darkorange',
    'Flying': 'skyblue',
    'Poison': 'darkorchid',
    'Ground': 'goldenrod',
    'Rock': 'tan',
    'Bug': 'yellowgreen',
    'Ghost': 'slateblue',
    'Steel': 'darkgray',
    'Fire': 'orangered',
    'Water': 'dodgerblue',
    'Grass': 'limegreen',
    'Electric': 'gold',
    'Psychic': 'palevioletred',
    'Ice': 'powderblue',
    'Dragon': 'royalblue',
    'Dark': 'dimgray',
    'Fairy': 'lightpink',
}

    # Crie uma lista de cores com base nos tipos
    cores = []
    
    #Porém temos casos de tipos duplos
    for t in tipos:
        if t.split(",")[1].strip() != "":
            cor1 = cores_pokemon[t.split(",")[0].strip()]
            cor2 = cores_pokemon[t.split(",")[1].strip()]
            # Use uma média ponderada das cores para criar um gradiente
            cor = np.mean([np.array(matplotlib.colors.to_rgba(cor1)), np.array(matplotlib.colors.to_rgba(cor2))], axis=0)
            cores.append(cor)
        
        else:
            cores.append(cores_pokemon[t.split(",")[0]])
    
    #Retira as vírgulas
    for i, t in enumerate(tipos, start=0): 
        if t.split(",")[1].strip() != "":
            tipos[i] = t.split(",")[0].strip()+"/"+t.split(",")[1].strip()
        else:
            tipos[i] = t.split(",")[0].strip()
            
    # Criar o gráfico de pizza
    legend_patches = [mpatches.Patch(color=color, label=tipo) for tipo, color in cores_pokemon.items()]
    plt.pie(quantidades, autopct='%1.1f%%', startangle=140, colors=cores)
    plt.axis('equal')  # Equaliza o aspecto para que o gráfico de pizza seja circular
    plt.title('Distribuição de Tipos de Pokémon na região')
    # Adicionar a legenda
    plt.legend(handles=legend_patches, bbox_to_anchor=(1, 0.5), loc='center left')
    plt.show()

def plot_encounter_rate(rates, names):
    
    #Plota um gráfico mostrando os pokèmons mais prováveis de aparecer de acordo com seu tipo.
    
    # Criar gráfico de barras
    plt.bar(names, rates, color='skyblue')
    plt.xlabel('Pokémon')
    plt.ylabel('Taxa de Encontro (%)')
    plt.title('Taxa de Encontro por Pokémon')
    
    # Rotacionar os rótulos no eixo x em 45 graus
    plt.xticks(rotation=45, ha='right')
    
    plt.show()

def plot_encounter_heatmap(effectiveness, resistance):
    #effectiveness e resisteance são dicionários
    

    # Crie os DataFrames
    df1 = pd.DataFrame([effectiveness])
    df2 = pd.DataFrame([resistance])

    
    # Exiba as primeiras linhas dos DataFrames para verificar se estão corretos
    print(df1.head())
    print(df2.head())
    
    cores_pokemon = {
    'Normal': 'lightgrey',
    'Fighting': 'darkorange',
    'Flying': 'skyblue',
    'Poison': 'purple',
    'Ground': 'saddlebrown',
    'Rock': 'dimgray',
    'Bug': 'limegreen',
    'Ghost': 'darkviolet',
    'Steel': 'silver',
    'Fire': 'orangered',
    'Water': 'dodgerblue',
    'Grass': 'limegreen',
    'Electric': 'gold',
    'Psychic': 'mediumvioletred',
    'Ice': 'lightcyan',
    'Dragon': 'royalblue',
    'Dark': 'black',
    'Fairy': 'lightpink',
}
    
    #palheta de cores
    custom_cmap = sns.color_palette(list(cores_pokemon.values()))
    
    plt.figure(figsize=(10, 8))
   
    # Crie um mapa de calor para as taxas de encontro
    sns.heatmap(df1.corr(), annot=True, cmap=custom_cmap, cbar=False)
    
    # Adicione rótulos aos eixos
    plt.xticks(ticks=range(len(resistance)), labels=effectiveness.keys(), rotation=45, ha='right')
    plt.yticks(ticks=range(len(effectiveness)), labels=effectiveness.keys())

    plt.title('Correlação entre Efetividade')
    plt.show()
    
    sns.heatmap(df2.corr(), annot=True, cmap=custom_cmap, cbar=False)
    # Adicione rótulos aos eixos
    plt.xticks(ticks=range(len(resistance)), labels=resistance.keys(), rotation=45, ha='right')
    plt.yticks(ticks=range(len(effectiveness)), labels=resistance.keys())

    plt.title('Correlação entre Resistência')
    
    plt.show()
    
    
main(tipos_pokemon)    
