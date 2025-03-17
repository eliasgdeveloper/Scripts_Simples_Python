# Lista de produtos e preços
Lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
Preços = [2000, 9000, 6000, 11000]
dic_produtos = {"airpod": 2000, "ipad": 9000, "iphone": 6000, "macbook": 11000}

# Solicitar entrada do usuário para nome e preço do produto
nome_produto = input("Nome do produto: ").strip().lower()
preço_produto = input("Preço do produto: ").strip()

# VALIDAÇÃO ADICIONADA: VERIFICA SE O PREÇO É UM NÚMERO VÁLIDO ANTES DE CONVERTÊ-LO
if preço_produto.replace('.', '', 1).isdigit():
    preço_produto = float(preço_produto)  # Converte para float
else:
    print("Erro: O preço deve ser um número válido.")
    exit()  # Sai do programa se a entrada for inválida

# REMOVIDA LINHA REDUNDANTE QUE CONVERTIA NOVAMENTE `nome_produto` PARA MINÚSCULO
# nome_produto = nome_produto.lower()

# CORREÇÃO: `dic_produtos[Nome_produto]` FOI AJUSTADO PARA `dic_produtos[nome_produto]` E `Preço_produto` PARA `preço_produto`
dic_produtos[nome_produto] = preço_produto
print(dic_produtos)

# Atualizar o preço de todos os produtos em 10% no final
# REMOVIDO O TRECHO DUPLICADO QUE ATUALIZAVA O PREÇO DO PRODUTO "AIRPOD" DUAS VEZES
for produto in dic_produtos:
    novo_preço = dic_produtos[produto] * 1.1  # Calcula 10% a mais
    dic_produtos[produto] = novo_preço  # Atualiza o preço no dicionário

# EXIBE O DICIONÁRIO COM OS PREÇOS ATUALIZADOS
print(dic_produtos)

# Lista de produtos e preços
dic_produtos = {"airpod": 2000, "ipad": 9000, "iphone": 6000, "macbook": 11000}

# Função para calcular o preço com imposto
def calcular_preco_com_imposto(preco, taxa=0.1):
    return preco * (1 + taxa)

# Exibir opções para o usuário
print("Opções:")
print("1. Digite um produto para ver seu preço com imposto.")
print("2. Ver todos os produtos com preços normais e preços com imposto.")
opcao = input("Escolha uma opção (1 ou 2): ").strip()

if opcao == "1":
    # Buscar um único produto
    nome_produto = input("Digite o nome do produto: ").strip().lower()
    if nome_produto in dic_produtos:
        preco_original = dic_produtos[nome_produto]
        preco_com_imposto = calcular_preco_com_imposto(preco_original)
        print(f"Produto: {nome_produto.capitalize()}")
        print(f"Preço original: R$ {preco_original:.2f}")
        print(f"Preço com imposto: R$ {preco_com_imposto:.2f}")
    else:
        print("Produto não encontrado.")
elif opcao == "2":
    # Mostrar todos os produtos com preços normais e com imposto
    print(f"{'Produto':<15}{'Preço Original':<20}{'Preço com Imposto':<20}")
    for produto, preco in dic_produtos.items():
        preco_com_imposto = calcular_preco_com_imposto(preco)
        print(f"{produto.capitalize():<15}R$ {preco:<20.2f}R$ {preco_com_imposto:<20.2f}")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")







