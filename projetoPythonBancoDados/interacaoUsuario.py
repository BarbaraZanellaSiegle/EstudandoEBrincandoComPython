from time import sleep
import sqlite3

def menu_interacao():

    loop = True

    while loop != False:
        continuarSair = int(input(f"Deseja continuar ou sair do Sistema?\nDigite 1 para Continuar e 2 para Sair: "))

        if continuarSair == 1:
            print("Você Continuou!")
            print("Verificado se existem tabelas no banco!")

            conexao = sqlite3.connect("VamosBricar.sqlite")
            cursor = conexao.cursor()

            comando = "SELECT * FROM sqlite_master where type='table';"
            cursor.execute(comando)

            tabelas = cursor.fetchall()

            if tabelas:
                for tabela in tabelas:
                    print("LISTA DE TABELAS:")
                    print(f"Tabela:", tabela[1])
            else:
                print("Nenhuma Tabela encontrada no banco atual")

            conexao.commit()
            conexao.close()
         


            #Criando tabelas
            criarTabela = int(input(f"Deseja criar uma tabela?\nDigite 1 para Sim e 2 para Não: "))
            if criarTabela == 1:
                print("Criando tabelas...")
            
            elif criarTabela == 2:
                print("Ok, não será criado novas tabelas!")
            
            else:
                print("Não foi informado uma opção valida!")


            #Deletando tabelas
            deletarTabela = int(input(f"Deseja deletar uma tabela?\nDigite 1 para Sim e 2 para Não: "))

            if deletarTabela == 1:
                print("Deletando tabelas...")
            
            elif deletarTabela == 2:
                print("Ok, não será deletado nenhuma tabela!")
            
            else:
                print("Não foi informado uma opção valida!")


            loop = True



        elif continuarSair == 2:

            for animacao in range(10):
                sleep(0.3)
                print("*")
                
            print("Você Saiu!")

            loop = False



        else:
            print("Informe uma opção valida!")
            loop = True




