mostrar_lista = ["Pao", "Leite", "Queijo", "Chapa Eletrolux","Abacaxi", "Pacoca", "Energético" ]

def Lista():
    print ("Sua Lista de compras é")

    for indice, item  in enumerate(mostrar_lista):
        print (f"Posição {indice}: {item}")

def Cadastrar():
    adicionar = input("O que deseja adicionar??")
    mostrar_lista.append(adicionar)
     
    print (f"Seu item {adicionar} foi adicionado a lista!!")

def Excluir ():
    excluir = input ("O que deseja excluir??")
    mostrar_lista.remove(excluir)

    print (f"Perfeito, seu item {excluir} foi retirado da lista!!")

def Modificar ():
    modificar = input ("O que deseja Modificar??")
    posicao = mostrar_lista.index(modificar)
    novo_item = input ("Qual seria o novo item??")
    mostrar_lista[posicao] = novo_item

    print (f"Perfeito, seu item {modificar} foi alterado!!!")


while True:
    print ("LISTA DE COMPRAS!!")
    print ("1 - Mostrar Lista!")
    print ("2 - Cadastrar Item na Lista")
    print ("3 - Excluir Item na Lista")
    print ("4 - Modificar Item na Lista")
    print ("5 - Sair")
    
    opcao = input ("Escolha uma opção!!")


    if opcao == "1":
        Lista()

    elif opcao == "2":
        Cadastrar()

    elif opcao == "3":
        Excluir()

    elif opcao == "4":
        Modificar()

    elif opcao == "5":
        break

    else:
        print("Opção inválida!!")
