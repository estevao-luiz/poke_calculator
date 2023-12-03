from tkinter import * 
from tkinter import messagebox 
import code as cd
import interactive_map as mp

#version = ""
#province = "" 
#area = "" 
#biome = "" 
#party = []

class PokemonApp(Tk):
        def __init__(self):
            super().__init__()
            self.title("Pokemon App")
            self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
           
            #Adicione um atributo de instância para armazenar a province
            self.version  = mp.version_value 
            self.province = mp.province_value 
            self.area = mp.area_value 
            self.biome  = mp.biome_value
            
            print(self.version, self.province, self.area, self.biome)
            
            #Criando os frames
            #self.column1 = Frame(self)
            #self.column1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
            #self.column2 = Frame(self)
            #self.column2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    
            # Labels e Entries na coluna 1
            #labels_column = ["Escolha a versão da Pokedex:", "Escolha a área:", "Escolha o bioma:"]
            #for row, label_text in enumerate(labels_column):
            #   label = Label(self, text=label_text)
            #   label.grid(row=row, column=0, sticky="w", pady=5)
            #   entry = Entry(self)
            #   entry.grid(row=row, column=1, pady=5)
            
            #Adiciona coluna vazia    
            self.grid_columnconfigure(2, weight=1)
    
            #Labels e Entries na coluna 2
            label_team = Label(self, text="Equipe de Pokémon:")
            label_team.grid(row=0, column=3, sticky="w", pady=5)
    
            pokemon_entries = []
            for i in range(1, 7):
                label = Label(self, text=f"Pokémon {i}:")
                label.grid(row=i, column=3, sticky="w", pady=5)
                entry = Entry(self)
                entry.grid(row=i, column=4, pady=5)
                pokemon_entries.append(entry)
    
            # Botão
            self.button_submit = Button(self, text="Submit", command=lambda: self.show_team(pokemon_entries))
            self.button_submit.grid(row=1, column=5, padx=10, pady=10)
            
            
            
        def show_team(self, pokemon_entries):
                
                #version_entry = self.grid_slaves(row=0, column=1)  # Acessa o primeiro widget da lista
                #version = str(version_entry[0].get())
                
                #area_entry = self.grid_slaves(row=1, column=1)
                #area = str(area_entry[0].get())
                
                #biome_entry = self.grid_slaves(row=2, column=1)
                #biome = (biome_entry[0].get())
                
                team = [entry.get() if entry else "" for entry in pokemon_entries] + [""]*(6-len(pokemon_entries))
                
                Tk.destroy(self)
                
                result = main(self.version, self.province, self.area, self.biome, team)  # Captura o resultado e a mensagem
                        
                #Exibe a mensagem com o resultado
                messagebox.showinfo("Uma equipe play destroy é:", f"{result}")                       
            
def main(version, province, area, biome, party):
    test1 = cd.poke_finder(area, province, version)
    test2, test3 = cd.asses_encounter(test1, biome)
    test4 = cd.calculate_rate(test2[0], test2[1], test3)
    test5 = cd.types(test4)
    test6 = cd.asses_damage(test5)
    test7 = cd.ideal_party(test6)
    calculum = cd.compare_parties(party, test7)
    print(calculum)
    
    return calculum
    
#Garante que o progrma seja executado apenas quando exe for executado diretamente.        
if __name__ == "__main__":
    app = PokemonApp()
    app.mainloop()
