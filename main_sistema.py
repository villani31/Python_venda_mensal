import funcoes_sistema
import os

# valida usuario e senha do sistema
os.system("clear") or None
print("+".ljust(28,"-"),"+")
print("| Controle de vendas mensais |")
print("+".ljust(28,"-"),"+")
usuario = input("Login do sistema: ")
senha = input("Senha do sistema: ")
os.system("clear") or None
funcoes_sistema.validaAcesso(usuario,senha)