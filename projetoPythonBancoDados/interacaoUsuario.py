from time import sleep
import sqlite3
from Crud import chamafuncao, listarTabela, animacao, interacaoBanco

def menu_interacao():
    
    chamafuncao()
    
    loop = True

    while loop != False:
        continuarSair = int(input(f"Deseja continuar ou sair do Sistema?\nDigite 1 para Continuar e 2 para Sair: "))

        if continuarSair == 1:
            print("Você Continuou!")
            print("Verificando se existem tabelas no banco...")

            conexao = sqlite3.connect("VamosBricar.sqlite")
            cursor = conexao.cursor()

            listarTabela(cursor, conexao)

            conexao.commit()
            conexao.close()
         

            interacaoBanco()




        elif continuarSair == 2:

            animacao()                
            print("Você Saiu!")
            loop = False



        else:
            print("Informe uma opção valida!")
            loop = True




