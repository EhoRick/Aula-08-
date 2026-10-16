import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

lista_produtos = carregar_produtos()

def cadastrar_produtos():
   
   id = int(input("Qual é o id??: "))
   nome = input("Qual seria o produto??: ")
   categoria = input("Qual a categoria do produto??: ")
   preco = int(input("Qual o preço dele??: "))
   estoque = int(input("Quantos dele haverá no estoque??: "))
   
   lista_produtos.append({
       "id": id,
       "nome": nome,
       "categoria": categoria,
       "preco": preco,       
       "estoque": estoque    
   })
   print(f"\n {nome} adicionado com sucesso!")
   
   salvar_produtos(lista_produtos)
   

def remover_produtos():
    id = int(input("Qual o id do produto que deseja remover??: "))
    nome = input("Qual o nome do produto que deseja remover??: ")
    categoria = input("Qual a categoria do produto que deseja remover??: ")
    preco = int(input("Qual o preço do produto que deseja remover??: "))
    estoque = int(input("Quantos dele há no estoque para remover??: "))

    lista_produtos.remove({
        "id": id,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque
    })
    print(f"\n {nome} foi removido com sucesso!")

    salvar_produtos(lista_produtos)

def modificar_produtos():
    def modificar_produtos():
        print("\n--- MODIFICAR PRODUTO ---")
    id = int(input("Digite o ID do produto que deseja modificar: "))
    
    produto_encontrado = False

    
    for item in lista_produtos:
        if item["id"] == id:
            print(f"\nProduto encontrado: {item['nome']}")
            print("Agora, digite os novos dados:")
            
            
            item["nome"] = input("Qual o novo nome?: ")
            item["categoria"] = input("Qual a nova categoria?: ")
            item["preco"] = int(input("Qual o novo preço?: "))
            item["estoque"] = int(input("Qual o novo estoque?: "))
            
            produto_encontrado = True
            print(f"\n {item['nome']} foi modificado com sucesso!")
            break 

    
    if not produto_encontrado:
        print("Produto não encontrado com esse ID!")

    
    salvar_produtos(lista_produtos)

while True:
  print("---> CONTROLE DE ESTOQUES <---")
  print("1 - Mostrar todos os produtos do Estoque: ")
  print("2 - Cadastrar um novo produto no Estoque: ")
  print("3 - Remover um Item do Estoque: ")
  print("4 - Modificar um Item no Estoque: ")
  print("0 - Sair: ")

  opcao = input("Escolha uma opção: ")

  if opcao == "1":
        print("\n--- PRODUTOS EM ESTOQUE ---")
        if not lista_produtos:
            print("O estoque está vazio.")
        else:

            for indice, item in enumerate(lista_produtos):
                print(f"Posição {indice}: {item['nome']} (Preço: {item['preco']} | Estoque: {item['estoque']})")
        
  elif opcao == "2":
      cadastrar_produtos()
        
  elif opcao == "3":
      remover_produtos()
    

  elif opcao == "4":
      modificar_produtos()
        

  elif opcao == "0":
        break

