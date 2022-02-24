states_of_america = ["Delaware", "Alaska", "Pennsylvania", "South Carolina"]

print(states_of_america[0]) # imprime primeiro item da lista

print(states_of_america[-1]) # imprime o último item da lista

states_of_america[2] = "Pencilvania" # altera o valor

print(states_of_america[2])

states_of_america.append("Michigan") # adiciona item no fim da lista

print(states_of_america[-1])

# adiciona vários itens no fim da lista
states_of_america.extend(["Teste1", "Teste2", "Teste3", "Teste4"])

print(states_of_america)
