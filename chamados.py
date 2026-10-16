chamados = [
  { "id": 1, "titulo": "Erro no login", "prioridade": "Alta", "status": "Aberto", "usuario": "Ana Silva" },
  { "id": 2, "titulo": "Tela branca no app", "prioridade": "Crítica", "status": "Aberto", "usuario": "Bruno Costa" },
  { "id": 3, "titulo": "Atualizar cadastro", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Carlos Souza" },
  { "id": 4, "titulo": "Boleto não gerado", "prioridade": "Média", "status": "Aberto", "usuario": "Daniela Lima" },
  { "id": 5, "titulo": "Botão quebrado", "prioridade": "Baixa", "status": "Aberto", "usuario": "Eduardo Rocha" },
  { "id": 6, "titulo": "Lentidão na busca", "prioridade": "Média", "status": "Em progresso", "usuario": "Fernanda Alves" },
  { "id": 7, "titulo": "Recuperar senha", "prioridade": "Alta", "status": "Aberto", "usuario": "Gabriel Santos" },
  { "id": 8, "titulo": "Erro no Pix", "prioridade": "Crítica", "status": "Aberto", "usuario": "Amanda Melo" },
  { "id": 9, "titulo": "Mudar foto de perfil", "prioridade": "Baixa", "status": "Fechado", "usuario": "Igor Ribeiro" },
  { "id": 10, "titulo": "Exportar PDF falhou", "prioridade": "Média", "status": "Aberto", "usuario": "Juliana Vieira" },
  { "id": 11, "titulo": "Carrinho esvaziando", "prioridade": "Alta", "status": "Em progresso", "usuario": "Lucas Martins" },
  { "id": 12, "titulo": "Cupom inválido", "prioridade": "Média", "status": "Aberto", "usuario": "Mariana Dias" },
  { "id": 13, "titulo": "Página 404 no FAQ", "prioridade": "Baixa", "status": "Aberto", "usuario": "Nicolas Ferreira" },
  { "id": 14, "titulo": "Atraso na entrega", "prioridade": "Alta", "status": "Aberto", "usuario": "Patricia Gomes" },
  { "id": 15, "titulo": "Email de boas-vindas", "prioridade": "Baixa", "status": "Fechado", "usuario": "Rodrigo Ramos" },
  { "id": 16, "titulo": "Estorno pendente", "prioridade": "Alta", "status": "Em progresso", "usuario": "Sabrina Oliveira" },
  { "id": 17, "titulo": "Alerta de segurança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Thiago Barbosa" },
  { "id": 18, "titulo": "Link quebrado no menu", "prioridade": "Baixa", "status": "Aberto", "usuario": "Vanessa Cunha" },
  { "id": 19, "titulo": "Nota fiscal sumiu", "prioridade": "Média", "status": "Aberto", "usuario": "Willian Cardoso" },
  { "id": 20, "titulo": "Modo escuro travando", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Yasmim Lopes" },
  { "id": 21, "titulo": "Erro na API de CEP", "prioridade": "Alta", "status": "Aberto", "usuario": "Arthur Antunes" },
  { "id": 22, "titulo": "Notificação duplicada", "prioridade": "Baixa", "status": "Aberto", "usuario": "Beatriz Mendes" },
  { "id": 23, "titulo": "Sessão expirando rápido", "prioridade": "Média", "status": "Em progresso", "usuario": "Caio Nogueira" },
  { "id": 24, "titulo": "Erro no cartão de crédito", "prioridade": "Crítica", "status": "Aberto", "usuario": "Diana Prince" },
  { "id": 25, "titulo": "Traduzir termo em inglês", "prioridade": "Baixa", "status": "Fechado", "usuario": "Elton John" },
  { "id": 26, "titulo": "Chat de suporte offline", "prioridade": "Alta", "status": "Aberto", "usuario": "Fábio Assunção" },
  { "id": 27, "titulo": "Upload de comprovante", "prioridade": "Média", "status": "Aberto", "usuario": "Gisele Bündchen" },
  { "id": 28, "titulo": "Histórico sumiu", "prioridade": "Alta", "status": "Em progresso", "usuario": "Heitor Villa" },
  { "id": 29, "titulo": "Termos de uso desatualizados", "prioridade": "Baixa", "status": "Aberto", "usuario": "Isabela Garcia" },
  { "id": 30, "titulo": "Erro 500 no checkout", "prioridade": "Crítica", "status": "Aberto", "usuario": "Jorge Ben" },
  { "id": 31, "titulo": "Ajustar margem do header", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Karina Bacchi" },
  { "id": 32, "titulo": "Filtro por data quebrado", "prioridade": "Média", "status": "Aberto", "usuario": "Leonardo Dicaprio" },
  { "id": 33, "titulo": "Assinatura não renovada", "prioridade": "Alta", "status": "Aberto", "usuario": "Marta Vieira" },
  { "id": 34, "titulo": "Áudio do vídeo não funciona", "prioridade": "Média", "status": "Aberto", "usuario": "Neymar Junior" },
  { "id": 35, "titulo": "Atualizar política de privacidade", "prioridade": "Baixa", "status": "Fechado", "usuario": "Otávio Mesquita" },
  { "id": 36, "titulo": "Queda do servidor interno", "prioridade": "Crítica", "status": "Em progresso", "usuario": "Paula Toller" },
  { "id": 37, "titulo": "Convite por email falhou", "prioridade": "Baixa", "status": "Aberto", "usuario": "Quintino Aires" },
  { "id": 38, "titulo": "Extrato em branco", "prioridade": "Alta", "status": "Aberto", "usuario": "Renata Vasconcellos" },
  { "id": 39, "titulo": "ícone errado no painel", "prioridade": "Baixa", "status": "Aberto", "usuario": "Samuel Rosa" },
  { "id": 40, "titulo": "Duplicidade de cobrança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Tais Araújo" },
  { "id": 41, "titulo": "Validação de CNPJ", "prioridade": "Média", "status": "Em progresso", "usuario": "Umberto Eco" },
  { "id": 42, "titulo": "Mensagem de erro confusa", "prioridade": "Baixa", "status": "Aberto", "usuario": "Valéria Valenssa" },
  { "id": 43, "titulo": "Problema com fonte negrito", "prioridade": "Baixa", "status": "Aberto", "usuario": "Wagner Moura" },
  { "id": 44, "titulo": "Links de redes sociais fora do ar", "prioridade": "Média", "status": "Aberto", "usuario": "Xuxa Meneghel" },
  { "id": 45, "titulo": "Sem sinal de geolocalização", "prioridade": "Alta", "status": "Em progresso", "usuario": "Yuri Gagarin" },
  { "id": 46, "titulo": "Página recarregando sozinha", "prioridade": "Alta", "status": "Aberto", "usuario": "Zeca Pagodinho" },
  { "id": 47, "titulo": "Gráfico de vendas travado", "prioridade": "Média", "status": "Aberto", "usuario": "Alinne Moraes" },
  { "id": 48, "titulo": "Impossível remover endereço", "prioridade": "Média", "status": "Em progresso", "usuario": "Beto Jamaica" },
  { "id": 49, "titulo": "Vazamento de memória na aba", "prioridade": "Crítica", "status": "Aberto", "usuario": "Cláudia Raia" },
  { "id": 50, "titulo": "Ajustar alinhamento do rodapé", "prioridade": "Baixa", "status": "Fechado", "usuario": "Dado Dolabella" }
]


# 1- Pesquisa por Usuário
# 2- Pesquisa por Prioridade
# 3- Pesquisa por Status
# 4- Pesquisa por Chamados Urgentes (prioridade e status, Crítica e Abertos)
# 5- Abrir chamado 
# 6- Resolver chamado (Em progresso)
# 7- Fechar chamado
# 0- Sair do Sistema



while True:
  print("---> LISTA DE CHAMADOS <---")
  print("1 - Pesquisar por Usuários")
  print("2 - Pesquisar por Prioridade")
  print("3 - Pesquisa por Status")
  print("4 - Pesquisa por Chamados Urgentes")
  print("5 - Abrir um Chamado")
  print("6 - Resolver um Chamado")
  print("7 - Fechar um Chamado")
  print("0 - Sair")

  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    chamar_usuario = input ("Qual seria o Usuário? ")
    for chamado in chamados:
      if chamado ["usuario"] == chamar_usuario:
        print (chamado)
      
  elif opcao == "2":
    nivel_prioridade = input ("Qual seria o nível de Prioridade? ")
    for chamado in chamados:
      if chamado ["prioridade"] == nivel_prioridade:
        print (chamado)

  elif opcao == "3":
    status_processo = input ("Qual é o Status atual? ")
    for chamado in chamados:
      if chamado ["status"] == status_processo:
        print (chamado)
    
  elif opcao == "4":
    for chamado in chamados:
      if chamado["status"] == "Aberto" and chamado["prioridade"] == "Crítica":
        print({chamado["id"]}, {chamado["titulo"]}, {chamado["status"]}, {chamado["prioridade"]})
      
  elif opcao == "5":
    pergunta_titulo = input("Qual chamada você gostaria de adicionar? ")
    pergunta_prioridade = input("Qual prioridade deseja adicionar? ")
    pergunta_status = input("Como está seu chamado?")
    pergunta_usuario = input("Qual o usuario? ")
    novo_id = chamados [-1] ['id'] + 1 if chamados else 1

    cadastrar = {
      "id": novo_id,
      "titulo": pergunta_titulo,
      "prioridade": pergunta_prioridade,
      "status": pergunta_status,
      "usuario": pergunta_usuario
    }
    chamados.append(cadastrar)
    print(chamados)
  
  elif opcao == "6":
    
    id_resolver = int(input("Digite o ID do chamado em progresso que deseja resolver: "))
    encontrado = False

    for chamado in chamados:
      if chamado["id"] == id_resolver:
        encontrado = True
        if chamado["status"] == "Em progresso":
          chamado["status"] = "Fechado"  
          print(f"Chamado #{chamado['id']} ('{chamado['titulo']}') foi resolvido e finalizado com sucesso")
        else:
          print(f"O chamado #{chamado['id']} não está 'Em progresso' (Status atual: {chamado['status']})")
        break

    if not encontrado:
      print("Seu chamado não foi encontrado")

  elif opcao == "7":

    id_fechar = int(input("Digite o ID do chamado que deseja finalizar: "))
    encontrado = False

    for chamado in chamados:
      if chamado["id"] == id_fechar:
        chamado["status"] = "Fechado"
        print(f"Chamado #{chamado['id']} ('{chamado['titulo']}') foi finalizado")
        encontrado = True
        break

    if not encontrado:
      print("Seu chamado não foi encontrado")
        
    elif opcao == "0":
      break
    else:
      print("Opção inválida, tente novamente.")
