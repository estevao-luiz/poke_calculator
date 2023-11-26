import json
import sys
import re 
import random 
import data_visual as dv


version = ""
province = "" 
area = "" 
biome = "" 
party = ""

def main():
  
    #version = input("Which of Paldean Pokedex do you play in? Scarlet or Violet \nAnswer with S or V\n")
    #version = "Scarlet"
    #province = input("Which of Province of Pandean Map are you in? \nExample: South Province\n")
    #province = "South"
    #area = input("Which of area of Paldean Province are you in? \nExample: Area One\n")
    #area = "One"
    #biome = str(input("Which of biomes are you in? \nExample: Grass\n"))
    #biome = "Grass"
    
    #party = ["Pikachu", "", "", "", "", ""]
    
    #Leitura da equipe
    #for i in range(6):
        #n = i+1
        #Partner = input(f"What is your current party? Pokémon number {n} \nFirst letter always capitalized\n")
        #party[i] = Partner
        
    #lineindex = encounter_biome(Version, Province, Area, Biome)    
    #print(lineindex)
    
    test1 = poke_finder(area, province, version)
    #print(test1)
    #print(len(test1))
    test2, test3 = asses_encounter(test1, biome)
    #print(test2, test3)
    test4 = calculate_rate(test2[0], test2[1], test3)
    test5 = types(test4)
    #print(test5)
    #from dano import asses_damage
    
    test6 = asses_damage(test5)
    #print(test6)
    test7 = ideal_party(test6)
    print("Uma possível equipe:")
    
    #test7_str = json.dumps(list(test7.values()), ensure_ascii=False) 
    #print(test7_str)
    
    test8 = compare_parties(party, test7)
    print(test8)
    
    result = test8
   
    
    
def asses_damage(typing):
    
    from collections import defaultdict
    
    type1 = typing[0]
    type2 = typing[1]
    
    # Dicionário de tipos e seus fatores de dano
    type_damage = {
    "Normal": {"Normal": 1, "Fighting": 1, "Flying": 1, "Poison": 1, "Ground": 1, "Rock": 0.5, "Bug": 1, "Ghost": 0, "Steel": 0.5, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Psychic": 1, "Ice": 1, "Dragon": 1, "Dark": 1, "Fairy": 1},
    "Fighting": {"Normal": 2, "Fighting": 1, "Flying": 0.5, "Poison": 0.5, "Ground": 1, "Rock": 2, "Bug": 0.5, "Ghost": 0, "Steel": 2, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Psychic": 0.5, "Ice": 2, "Dragon": 1, "Dark": 2, "Fairy": 0.5},
    "Flying": {"Normal": 1, "Fighting": 2, "Flying": 1, "Poison": 1, "Ground": 1, "Rock": 0.5, "Bug": 2, "Ghost": 1, "Steel": 0.5, "Fire": 1, "Water": 1, "Grass": 2, "Electric": 0.5, "Psychic": 1, "Ice": 1, "Dragon": 1, "Dark": 1, "Fairy": 1},
    "Poison": {"Normal": 1, "Fighting": 1, "Flying": 1, "Poison": 0.5, "Ground": 0.5, "Rock": 0.5, "Bug": 1, "Ghost": 0.5, "Steel": 0, "Fire": 1, "Water": 1, "Grass": 2, "Electric": 1, "Psychic": 1, "Ice": 1, "Dragon": 1, "Dark": 1, "Fairy": 2},
    "Ground": {"Normal": 1, "Fighting": 1, "Flying": 0, "Poison": 2, "Ground": 1, "Rock": 2, "Bug": 0.5, "Ghost": 1, "Steel": 2, "Fire": 2, "Water": 1, "Grass": 0.5, "Electric": 2, "Psychic": 1, "Ice": 1, "Dragon": 1, "Dark": 1, "Fairy": 1},
    "Rock": {"Normal": 1, "Fighting": 0.5, "Flying": 2, "Poison": 1, "Ground": 0.5, "Rock": 1, "Bug": 2, "Ghost": 1, "Steel": 0.5, "Fire": 2, "Water": 1, "Grass": 1, "Electric": 1, "Psychic": 1, "Ice": 2, "Dragon": 1, "Dark": 1, "Fairy": 1},
    "Bug": {"Normal": 1, "Fighting": 0.5, "Flying": 0.5, "Poison": 0.5, "Ground": 1, "Rock": 1, "Bug": 1, "Ghost": 0.5, "Steel": 0.5, "Fire": 0.5, "Water": 1, "Grass": 2, "Electric": 1, "Psychic": 2, "Ice": 1, "Dragon": 1, "Dark": 2, "Fairy": 0.5},
    "Ghost": {"Normal": 0, "Fighting": 1, "Flying": 1, "Poison": 1, "Ground": 1, "Rock": 1, "Bug": 1, "Ghost": 2, "Steel": 1, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Psychic": 2, "Ice": 1, "Dragon": 1, "Dark": 0.5, "Fairy": 1},
    "Steel": {"Normal": 1, "Fighting": 1, "Flying": 1, "Poison": 1, "Ground": 1, "Rock": 2, "Bug": 1, "Ghost": 1, "Steel": 0.5, "Fire": 0.5, "Water": 0.5, "Grass": 1, "Electric": 0.5, "Psychic": 1, "Ice": 2, "Dragon": 1, "Dark": 1, "Fairy": 2},
    "Fire": {"Normal": 1, "Fighting": 1, "Flying": 1, "Poison": 1, "Ground": 1, "Rock": 0.5, "Bug": 2, "Ghost": 1, "Steel": 2, "Fire": 0.5, "Water": 0.5, "Grass": 2, "Electric": 1, "Psychic": 1, "Ice": 2, "Dragon": 0.5, "Dark": 1, "Fairy": 1},
    "Water": {"Normal": 1, "Fighting": 1, "Flying": 1, "Poison": 1, "Ground": 2, "Rock": 2, "Bug": 1, "Ghost": 1, "Steel": 1, "Fire": 2, "Water": 0.5, "Grass": 0.5, "Electric": 1, "Psychic": 1, "Ice": 1, "Dragon": 0.5, "Dark": 1, "Fairy": 1},
    "Grass": {"Normal": 1, "Fighting": 1, "Flying": 0.5, "Poison": 0.5, "Ground": 2, "Rock": 2, "Bug": 0.5, "Ghost": 1, "Steel": 0.5, "Fire": 0.5, "Water": 2, "Grass": 0.5, "Electric": 1, "Psychic": 1, "Ice": 1, "Dragon": 0.5, "Dark": 1, "Fairy": 1},
    "Electric": {"Normal": 1, "Fighting": 1, "Flying": 2, "Poison": 1, "Ground": 0, "Rock": 1, "Bug": 1, "Ghost": 1, "Steel": 1, "Fire": 1, "Water": 2, "Grass": 0.5, "Electric": 0.5, "Psychic": 1, "Ice": 1, "Dragon": 0.5, "Dark": 1, "Fairy": 1},
    "Psychic": {"Normal": 1, "Fighting": 2, "Flying": 1, "Poison": 2, "Ground": 1, "Rock": 1, "Bug": 1, "Ghost": 1, "Steel": 0.5, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Psychic": 0.5, "Ice": 1, "Dragon": 1, "Dark": 0, "Fairy": 1},
    "Ice": {"Normal": 1, "Fighting": 1, "Flying": 2, "Poison": 1, "Ground": 2, "Rock": 1, "Bug": 1, "Ghost": 1, "Steel": 0.5, "Fire": 0.5, "Water": 0.5, "Grass": 2, "Electric": 1, "Psychic": 1, "Ice": 0.5, "Dragon": 2, "Dark": 1, "Fairy": 1},
    "Dragon": {"Normal": 1, "Fighting": 1, "Flying": 1, "Poison": 1, "Ground": 1, "Rock": 1, "Bug": 1, "Ghost": 1, "Steel": 0.5, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Psychic": 1, "Ice": 1, "Dragon": 2, "Dark": 1, "Fairy": 0},
    "Dark": {"Normal": 1, "Fighting": 0.5, "Flying": 1, "Poison": 1, "Ground": 1, "Rock": 1, "Bug": 1, "Ghost": 2, "Steel": 1, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Psychic": 2, "Ice": 1, "Dragon": 1, "Dark": 0.5, "Fairy": 0.5},
    "Fairy": {"Normal": 1, "Fighting": 2, "Flying": 1, "Poison": 0.5, "Ground": 1, "Rock": 1, "Bug": 1, "Ghost": 1, "Steel": 0.5, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Psychic": 1, "Ice": 1, "Dragon": 2, "Dark": 2, "Fairy": 1}
}   
    
    
    # Função auxiliar para calcular a eficácia
    
    def calculate_effectiveness(typing):
        effectiveness = defaultdict(float)
        resistance = defaultdict(float)
        immunity = defaultdict(float)
        for t1 in typing:
            if t1 in type_damage:
                for t2 in type_damage:
                        effectiveness[t2] += type_damage[t2][t1]
                        resistance[t2] += type_damage[t1][t2]
                        if type_damage[t1][t2] == 0:
                            immunity[t2] += type_damage[t1][t2]
        return effectiveness, resistance, immunity
    
    effectiveness1, resistance1, immunity1 = calculate_effectiveness(type1)
    effectiveness2, resistance2, immunity2 = calculate_effectiveness(type2)
    
    def combine_dicts(dict1, dict2): #vai combinar dois dicionários e retornar as chaves e seus valores multiplicados.
        result_dict = {}
        
        for key1, value1 in dict1.items():
            for key2, value2 in dict2.items():
                if key1 == key2: #evita que se duplique o tipo no identificador do dicionário.
                    new_key = key1
                else: 
                    new_key = f"{key1} , {key2}" #escreve a dupla tipagem
                new_value = value1 * value2
                if f"{key2} , {key1}" not in result_dict: #garante que não se repita estruturas como tipo1,tipo2 e tipo2,tipo1.
                    result_dict[new_key] = new_value
                elif int(new_value) > int(result_dict[f"{key2} , {key1}"]): #se o valor tipo2,tipo1 for maior que tipo1,tipo2 então subtitue na casa tipo1,tipo2.
                    result_dict[new_key] = result_dict.pop(f"{key2} , {key1}") #renomeia a chave
                    result_dict[new_key] = new_value
        
        return result_dict
    
    combo_effectiveness = combine_dicts(effectiveness1, effectiveness2)
    combo_effectiveness = {key: int(values) for key, values in combo_effectiveness.items()}
    #print(combo_effectiveness)
    
    #print(combo_effectiveness)
    #para que o segundo dicionário siga o mesmo padrão decrescente:
    for key in resistance1:
        resistance1[key] *= -1
    
    combo_resistance = combine_dicts(resistance1,resistance2)
    #print(combo_resistance)
    
    
    def swap_indices(dict1, dict2):

        #Esta função serve para fazer a ordem das tipagens ficar normalizadas nas chaves
        #Para evitar KeyError: b , a ou a , b quando for feita comparação entre chaves.
        
        new_dict2 = {}
    
        for key2, value2 in dict2.items():
        # Verifique se a chave do tipo "b , a" está no dicionário 1
            if key2 not in dict1:
                new_key2 = key2.split(' , ')[-1] + ' , ' + key2.split(' , ')[0]  #inverte a tipagem
                new_dict2[new_key2] = value2  # Adicione ao novo dicionário
            else:
                new_dict2[key2] = value2  # Mantenha a chave original

        return new_dict2
    
    combo_resistance = swap_indices(combo_effectiveness, combo_resistance)   
    
    combo_effectiveness_copy = combo_effectiveness.copy()    
    perfect_party = [""] * len(combo_effectiveness_copy)
    
    #dv.plot_encounter_heatmap(combo_effectiveness, combo_resistance)            
    

    for i in range(len(combo_effectiveness_copy)):
        for combo in combo_effectiveness_copy:
            max_effectiveness = max(combo_effectiveness, key=combo_effectiveness.get)
            max_resistant = max(combo_resistance, key=combo_resistance.get)
            values_max_effectiveness = max(combo_effectiveness.values())
            most_resistant = defaultdict(float)
            most_effectiveness = [key for key, value in combo_effectiveness.items() if value == values_max_effectiveness]
           
            for maxes in most_effectiveness:
                for resistance in combo_resistance: #criando um dicionário com as maiores resistências para fins de desempate.
                    if maxes == resistance:
                        most_resistant[resistance] = combo_resistance[maxes]
            
            if combo == max_effectiveness == max_resistant: #caso geral em que o tipo mais efetivo é também o mais reistente.
                perfect_party[i] = combo
                del combo_effectiveness[combo]
                del combo_resistance[combo]
                break
            
            elif combo in combo_effectiveness and combo in combo_resistance:
                #if combo_effectiveness[combo] == combo_effectiveness[max_effectiveness]:  
                        #verfifca se ainda está no dict de resistências pois pode ja ter sido deletado.
                        #if combo_resistance[combo] == combo_resistance[max_resistant]: 
                            perfect_party[i] = max(most_resistant)
                            del most_resistant[perfect_party[i]]
                            del combo_effectiveness[perfect_party[i]]
                            del combo_resistance[perfect_party[i]]
                            break
                            
    return perfect_party

def encounter_biome(v, p, a, b):
    
    #Esta função verfica em que província/área o bioma está localizado#
    
    name_file = "biomas.txt"
    
    #uso do try para testes de erro
    
    with open(name_file, encoding='utf-8', mode='r') as file:
        nlines = 1
        found = False
        
        # Itera pelas linhas do arquivo
        for line in file:
            if b in line:
                found = True
                break  # Se encontrou a palavra, podemos parar a busca
            
            nlines += 1
        
        if not found:
            print(f'O bioma "{b}" indicado não existe.')
            sys.exit()

       
    return line


def poke_finder(area, region, version):
        
        #Acha a(s) line em que se localiza os pokemon de certa região e devolve o nº da line e o nome do pokemon numa tupla 
        
    name_file = "encounter_info.txt"
    pokenumber = 0
        
    
    with open(name_file, encoding = 'utf-8', mode = 'r') as file:
        lines = file.readlines()
        lineindex = []
            
        #enumera cada linha além de capturar o conteúdo de cada uma
        for number_line, line in enumerate(lines, start=1):
            if f'{region} ({area})' in line:
                pokenumber = number_line - 6 
            
            if version in line and pokenumber == number_line - 8:
                condition = True
            else:
                condition = False   
            
            if condition:
                lineindex.append(pokenumber)
                
             

        if lineindex != []:
            return lineindex
        else:
            return f"A region '{region}' não foi encontrada no '{name_file}'."

    
    
    
def asses_encounter(pokelines, bio):
    
    #Acha a taxa de encontro do pokémon de acordo com o índice da linha.
    
    name_file = "encounter_info.txt"
   
    encounter_rate = []
    per_biome = []
    names = []
    line_encounter_rate = []
    line_per_biome = []
    
    
    with open(name_file, encoding = 'utf-8', mode = 'r') as file:
        lines = file.readlines()
                
        for line_found, line in enumerate(lines, start=1):
                    
            for pokeline in pokelines:
                
                if line_found == pokeline:
                    line_encounter_rate.append(line_found + 2) #cria uma lista com localização de todos os encounter rates.
                    line_per_biome.append(line_found + 5) #cria uma lista com a localização de todos os biome rates.
                    names.append(line.split(":")[0].strip())
        
        
        for line_found, line in enumerate(lines, start=1):
             
            for number_line in line_encounter_rate:
                
                if number_line == line_found: #pega o conteúdo pós ":"
                    encounter_rate.append(line.split(":")[1].strip())
        
        
        for line_found, line in enumerate(lines, start=1):
                         
            for number_line in line_per_biome:
                
                if number_line == line_found: #tal expressão regular localiza o conteúdo de um parenteses pós a ocorrência de uma palavra específica.
    
                    if bio in line:
                        pattern = re.search(rf'{bio}\s*\((.*?)\)', line)
                        bio_data =  int(pattern.group(1)) #encontra o padrão "'bio' ()" dentro da frase.
                        per_biome.append(bio_data)
                    
                    else:
                        per_biome.append(1)
    
    rates = [[encounter_rate, per_biome], names]
    
    return rates
            
          

def calculate_rate(number1, number2, name):
    
    #Esta função recebe duas listas com porcentagens e calcula a taxa de encontro de cada pokémon e rankeia os mais prováveis de ser encontrados em certa região.
    
    rate = []
    
    for i in range(0, len(number1), 1): #uso do range().
        rate.append((int(number1[i])/100)*(number2[i]/100)) #multiplica as taxas e adiciona na primeira "coluna" de uma nova lista rates.
    
    rate_desc = sorted(zip(rate,name), reverse=True) #zip combina as duas listas de forma que os nomes mudem de ordem de acordo com uma organização decrescente. 
    ranking = [[x[0] for x in rate_desc], [x[1] for x in rate_desc]]
    ranking[0] = [round(x*100, 2) for x in ranking[0]] #transforma os valores em porcentagem, arredondando com dois algarismos significativos.
    
    #print(ranking) 

    dv.plot_encounter_rate(ranking[0], ranking[1])
    
    return ranking

def types(ranking):
    
    #Esta função recebe uma lista com as porcentagens de encontro e nomes e retorna os tipos mais prováveis de aparecer.
    
    name_file = "pokémon.txt"
    poke_types = [[],[], ranking[1]]
    
    
    with open(name_file, encoding= 'utf-8', mode = 'r') as file:
        lines = file.readlines()
        
        for i in range(len(ranking[1])):
           
            for line in lines:
                
                if ranking[1][i] in line: #verifica se o nome do pokémon está na linha
                    type1 = line.split(",")[1].strip()
                    type2 = line.split(",")[2].strip()
                    poke_types[0].append(type1)
                    poke_types[1].append(type2)
    
    print(poke_types[0], poke_types[1])
    
    types_list = [f"{primary}, {secondary}" for primary, secondary in zip(poke_types[0], poke_types[1])]
    print(types_list)
    dv.main(types_list)
            
    return poke_types
                    
            
    
def ideal_party(typelist):
    
    #Esta função recebe uma lista ordenada em forma decrescente dos tipos mais 
    #adequados e retorna uma equipe perfeita de 6 pokémon de S/V.
    
    random.seed()
    
    name_file = "pokémon.txt"
    
    from collections import defaultdict
    
    perfect_party = defaultdict(lambda: [])
    better_pokes = defaultdict(lambda: []) 
    
    

    with open(name_file, encoding = 'utf-8', mode = 'r') as file:
        lines = file.readlines()
        
        new_typelist = []
        typelist_original = typelist.copy()
        
        for line in lines:
            for types in typelist: #Verifica se dado tipo está na pokedex de paldea.
                if types in line and line.split(" , ")[2].strip() == "": #localiza tipos únicos
                    new_typelist.append(types)
                    typelist.remove(types)
                elif types.count(" , ") == 1:
                    if all(type_ in line for type_ in types.split(" , ")): #localiza tipos duplos
                        new_typelist.append(types)
                        typelist.remove(types)
                    
        type_index = {type_: index for index, type_ in enumerate(typelist_original)}
        new_typelist.sort(key=lambda x: type_index.get(x, float('inf')), reverse=False)
        better_types = new_typelist[:6]
        
        for types in better_types:
            for poke in lines:
                if types in poke and poke.split(" , ")[2].strip() == "":
                    better_pokes[types].append(poke.split(" , ")[0].strip())
                elif types.count(" , ") == 1: 
                    if all(type_ in poke for type_ in types.split(" , ")):
                        better_pokes[types].append(poke.split(" , ")[0].strip())
        
                    
        #teste=list(better_pokes.values())
                   
        for types, pokes in better_pokes.items():

                perfect_party[types] = random.choice(pokes)
            
        
    return perfect_party            
                    

def compare_parties(atual, ideal):
   
    #Esta função recebe a equipe atual e a ideal e compara as duas e faz a devolutiva positiva(manutenção) ou negativa(troca) da equipe atual.
    
    from collections import defaultdict
    
    name_file = "pokémon.txt"
    
    types_atual = defaultdict(float)
   
    
    with open(name_file, encoding = 'utf-8', mode = 'r') as file:
        lines = file.readlines()
        
        for pokes in atual:
            pokemon_encontrado = False  # Inicializa como False para cada novo Pokémon

            for line in lines:
                if pokes != "":
                    if pokes in line:
                        types_atual[pokes] = line.split(" , ")[1].strip() + " , " + line.split(" , ")[2].strip()
                        pokemon_encontrado = True  # Marca que o Pokémon foi encontrado
        
            if pokes != "" and not pokemon_encontrado:
                return f"O pokémon {pokes} não se encontra em Paldea."
        
        
        
        for pokes_atuals, types_atuals  in types_atual.items():
            for types_ideals, pokes_ideals  in ideal.items():
               if  types_atuals == types_ideals: 
                   del ideal[types_atuals] 
               elif types_atuals.split(" , ")[-1]+" , "+types_atuals.split(" , ")[0] == types_ideals:
                   del ideal[types_atuals.split(" , ")[-1]+" , "+types_atuals.split(" , ")[0]]
        
        ideal_str = json.dumps(list(ideal.values()), ensure_ascii=False)
        atual_str = json.dumps(list(types_atual.keys()), ensure_ascii=False)
        
        if len(ideal) == 0:
            return f"A equipe {atual_str} já é ideal." #Caso em que a equipe ideal é a atual.
        elif len(ideal) == 6:
            return f"A equipe ideal é {ideal_str}." #Caso em que não é dado nenhum pokémon ou nenhum da equipe é ideal.
        elif len(ideal) >= 1:  
            return f"Para ficar ideal, à sua equipe {atual_str} deve ser adionados os pokémons {ideal_str}" #Caso em que a equipe já possui pokes ideais.
        
    
    
main()
