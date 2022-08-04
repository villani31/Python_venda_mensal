import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Funcoes sistema fincanceiro

valorvenda = []
mesvenda = []
valor = 0
user = "Admin"
passw = "thiago"

# validacao de acesso ao sistema
def validaAcesso(pusuario,psenha):
    contador = 2
    while (contador < 4):
        if ((pusuario == user) and (psenha == passw)):
            print("Login efeturado com sucesso...")
            break
        elif ((pusuario != user) or (psenha != passw)):
            print("Usuario/Senha inválido, tentativa de acesso",contador)
            pusuario = input("Login do sistema: ")
            psenha = input("Senha do sistema: ")
            contador += 1
            os.system("clear") or None
            if (contador == 4):
                print("-" * 40)
                print("Usuário bloqueado por tentativa")
                print("-" * 40)
                break
    if ((pusuario == user) and (psenha == passw)):
        menuPrincipal()

# funcao gera grafico
def graficovendas(pmesvenda,pvalorvenda):
    valores = list(zip(pmesvenda,pvalorvenda))
    df = pd.DataFrame(valores, columns=["Mes","Valor"])
    sns.barplot(x="Mes", y="Valor", data=df, color="c")
    plt.title("Gráfico de vendas mensal")
    plt.show()

# menu de acesso ao sistema
def menuPrincipal():
    opcao = 0
    mes = ""
    try:
        while (opcao != 6):
            os.system("clear") or None
            print("+".ljust(42,"-"),"+")
            print("| Sistema Financeiro - Controle de Vendas  |")
            print("+".ljust(42,"-"),"+")
            print("| 1 - Cadastrar       |     2 - Alterar    |")
            print("| 3 - Excluir         |     4 - Visualizar |")
            print("| 5 - Mostrar Gráfico |     6 - Encerrar   |")
            print("+".ljust(42,"-"),"+")
            opcao = int(input("Digite a opção desejada: "))
            global mesvenda
            if (opcao == 1):
                # Cadastrar
                mes = input("Qual o mês da venda para cadastrar: ")
                if (mes in mesvenda):
                    print("Mês já cadastrado.")
                else: 
                    mesvenda.append(mes)
                    valor = float(input("Qual o valor das venda no mês: "))
                    valorvenda.append(valor)
                    print("-" * 40)
                    print(">>>>> Cadastro feito com sucesso <<<<<")
                    print("-" * 40)
                    input("Pressione enter para continuar...")
                    os.system("clear") or None
            elif (opcao == 2):
                # Alterar
                mes = input("Qual mês deseja alterar o valor: ")
                if (mes in mesvenda):
                    for v in range(0,len(valorvenda)):
                        if (mes in mesvenda):
                            novovalor = float(input("Informe o novo valor para o mês "+ mes +": "))
                            valorvenda[v] = novovalor
                            print("-" * 40)
                            print(">>>>> Valor alterado com sucesso <<<<<")
                            print("-" * 40)
                            input("Pressione enter para continuar...")
                            break
                            os.system("clear") or None
                else:
                    print("-" * 40)
                    print(">>>>> Mês não cadastrado <<<<<")
                    print("-" * 40)
                    input("Pressione enter para continuar...")
                    os.system("clear") or None
            elif (opcao == 3):
                # Excluir
                mes = input("Qual mês deseja excluir: ")
                if (mes in mesvenda):
                    for v in range(0,len(mesvenda)):
                        if (mes == mesvenda[v]):
                            valorvenda.pop(v)
                    mesvenda.remove(mes)
                    print("-" * 40)
                    print(">>>>> Mês excluido com sucesso <<<<<")
                    print("-" * 40)
                    input("Pressione enter para continuar...")
                    os.system("clear") or None
                else:
                    print("-" * 40)
                    print(">>>>> Mês não cadastrado <<<<<")
                    print("-" * 40)
                    input("Pressione enter para continuar...")
                    os.system("clear") or None
            elif (opcao == 4):
                # Visualizar
                # criando uma lista de tuplas
                valores = list(zip(mesvenda,valorvenda))
                print("")
                print("--" * 12)
                df = pd.DataFrame(valores, columns= ["Mês","Valor"])
                print(df)
                print("--" * 12)
                print(">>>>> Relatório gerado com sucesso <<<<<")
                print("-" * 40)
                input("Pressione enter para continuar...")
                os.system("clear") or None
            elif (opcao == 5):
                # Mostrar grafico
                graficovendas(mesvenda,valorvenda)
            elif (opcao == 6):
                # Encerrar
                os.system("clear") or None
                print(">>>> Obrigado por usar o sistema <<<<")
            else:
                print(">>>> Opção invalida <<<<")
                input("Pressione enter para continuar...")
                os.system("clear") or None
    # Tratamento de erro
    except ValueError:
                print("-" * 40)
                print(">>>> Digite um número inteiro <<<<")
                print("-" * 40)
                input("Pressione enter para continuar...")
                # Chama a funcao de menu apos o erro
                menuPrincipal()