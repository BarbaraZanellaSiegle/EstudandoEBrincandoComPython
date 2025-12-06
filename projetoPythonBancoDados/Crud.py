import sqlite3
from time import sleep

def chamafuncao():
    print("Função chamada")


def listarTabela(cursor, conexao):
    comando = "SELECT * FROM sqlite_master where type='table';"
    cursor.execute(comando)

    tabelas = cursor.fetchall()

    if tabelas:
        for tabela in tabelas:
            print(f"Tabela:", tabela[1])
    else:
        print("Nenhuma Tabela encontrada no banco atual")


def animacao():
    for animacao in range(10):
        sleep(0.3)
        print("*")


def interacaoBanco(cursor, conexao):

    print("INTERAÇÃO COM O BANCO")

    conexao = sqlite3.connect("VamosBricar.sqlite")
    cursor = conexao.cursor()

    #Criando tabelas
    criarTabela = int(input(f"Deseja criar tabelas?\nDigite 1 para Sim e 2 para Não: "))
    if criarTabela == 1:

#        numeroTabelas = 1

#        while numeroTabelas != 5:
#            nomeTabela = input(f"Informe o nome da {numeroTabelas} tabela")

#           numeroColunas = 1
#            while numeroColunas != 5:
            
#                nomeColuna = input(f"Informe o nome da {numeroColunas} coluna da tabela {nomeTabela}")

#            comando_DDL = f'''CREATE TABLE IF NOT EXISTS {nomeTabela}(
#                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                        nome TEXT NOT NULL,
#                        preco REAL
#                        )'''

            comando_DDL = """
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT
                );

                CREATE TABLE IF NOT EXISTS fornecedor (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone REAL
                );

                CREATE TABLE IF NOT EXISTS categorias (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    descricao TEXT
                );

                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL,
                    categoria_id INTEGER,
                    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
                );

                CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    produto_id INTEGER NOT NULL,
                    cliente_id INTEGER NOT NULL,
                    fornecedor_id INTEGER NOT NULL,
                    quantidade INTEGER,
                    data TEXT,
                    FOREIGN KEY (produto_id) REFERENCES produtos(id),
                    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                    FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id)
                );
                """

            cursor.executescript(comando_DDL)
            conexao.commit()

            print("TABELAS CRIADAS!")


            novosDados = int(input(f"Deseja inserir, deletar ou alterar dados na tabela Produtos?\n(Digite 1 para Sim e 2 para Não)"))

            desejaInserirDeletar = True

            while desejaInserirDeletar != False:

                if novosDados == 2:
                    desejaInserirDeletar = False


                elif novosDados == 1:
                    insereDeleta = int(input("Deseja INSERIR dados, DELETAR dados, ALTERAR dados ou VOLTAR AO MENU ANTERIOR?\n(Digite 1 para Inserir, 2 para Deletar, 3 para ALTERAR e 4 para VOLTAR)"))

                    if insereDeleta == 1:

                        comando_DML_Insert = """
                        INSERT INTO clientes (nome, telefone) VALUES ('Ana Silva', '11987654321');
                        INSERT INTO clientes (nome, telefone) VALUES ('Carlos Almeida', '11988776655');
                        INSERT INTO clientes (nome, telefone) VALUES ('Fernanda Costa', '11999887766');
                        INSERT INTO clientes (nome, telefone) VALUES ('João Pereira', '21977665544');
                        INSERT INTO clientes (nome, telefone) VALUES ('Mariana Mendes', '31966554433');

                        
                        INSERT INTO fornecedor (nome, telefone) VALUES ('Fornecedor A', '1133221100');
                        INSERT INTO fornecedor (nome, telefone) VALUES ('Fornecedor B', '1144552211');
                        INSERT INTO fornecedor (nome, telefone) VALUES ('Fornecedor C', '1155663322');
                        INSERT INTO fornecedor (nome, telefone) VALUES ('Fornecedor D', '1166774433');
                        INSERT INTO fornecedor (nome, telefone) VALUES ('Fornecedor E', '1177885544');

                        
                        INSERT INTO categorias (nome, descricao) VALUES ('Bebidas', 'Produtos líquidos para consumo');
                        INSERT INTO categorias (nome, descricao) VALUES ('Limpeza', 'Produtos de higiene e limpeza');
                        INSERT INTO categorias (nome, descricao) VALUES ('Alimentos', 'Comida industrializada ou fresca');
                        INSERT INTO categorias (nome, descricao) VALUES ('Eletrônicos', 'Produtos elétricos e digitais');
                        INSERT INTO categorias (nome, descricao) VALUES ('Higiene', 'Produtos pessoais de higiene');

                        
                        INSERT INTO produtos (nome, preco, categoria_id) VALUES ('Coca-Cola 2L', 9.50, 1);
                        INSERT INTO produtos (nome, preco, categoria_id) VALUES ('Sabão em pó', 15.90, 2);
                        INSERT INTO produtos (nome, preco, categoria_id) VALUES ('Arroz 5kg', 22.70, 3);
                        INSERT INTO produtos (nome, preco, categoria_id) VALUES ('Fone Bluetooth', 79.90, 4);
                        INSERT INTO produtos (nome, preco, categoria_id) VALUES ('Shampoo 300ml', 12.40, 5);

                        
                        INSERT INTO pedidos (produto_id, cliente_id, fornecedor_id, quantidade, data)
                        VALUES (1, 1, 1, 2, '2025-01-10');

                        INSERT INTO pedidos (produto_id, cliente_id, fornecedor_id, quantidade, data)
                        VALUES (2, 2, 2, 1, '2025-01-12');

                        INSERT INTO pedidos (produto_id, cliente_id, fornecedor_id, quantidade, data)
                        VALUES (3, 3, 3, 5, '2025-01-15');

                        INSERT INTO pedidos (produto_id, cliente_id, fornecedor_id, quantidade, data)
                        VALUES (4, 4, 4, 1, '2025-01-20');

                        INSERT INTO pedidos (produto_id, cliente_id, fornecedor_id, quantidade, data)
                        VALUES (5, 5, 5, 3, '2025-01-22');
                        """


                        cursor.executescript(comando_DML_Insert)
                        conexao.commit()
                        # conexao.close()


                        print("Inserido Dados")

                        desejaInserirDeletar = True

                    
                    elif insereDeleta == 2:
                        comando_DML_Delete = """
                            DELETE FROM pedidos WHERE id = 3;
                            DELETE FROM pedidos WHERE id = 4;

                            DELETE FROM produtos WHERE preco > 20.00;

                            DELETE FROM categorias WHERE nome = 'Alimentos';
                            DELETE FROM categorias WHERE nome = 'Eletrônicos';

                            DELETE FROM fornecedor WHERE telefone = 1155663322;
                            DELETE FROM fornecedor WHERE nome = 'Fornecedor D';

                            DELETE FROM clientes WHERE id = 3;
                            DELETE FROM clientes WHERE telefone = 21977665544;
                            """
                        cursor.executescript(comando_DML_Delete)
                        
                        conexao.commit()
                        # conexao.close()

                        print("Deletado Dados")

                        desejaInserirDeletar = True


                    elif insereDeleta == 3:
                        comando_DML_Update = """
                            UPDATE clientes SET telefone = '11999998888' WHERE id = 1;
                            UPDATE clientes SET telefone = '21999997777' WHERE id = 2;

                            UPDATE fornecedor SET nome = 'Fornecedor 5' WHERE nome = 'Fornecedor E';
                            UPDATE fornecedor SET telefone = '21911113333' WHERE telefone = '1133221100';

                            UPDATE categorias SET descricao = 'Bebidas e sucos diversos' WHERE id = 5;
                            UPDATE categorias SET descricao = 'Higiene pessoal completa' WHERE id = 2;

                            UPDATE produtos SET preco = 10.99 WHERE preco < 15;

                            UPDATE pedidos SET quantidade = 10 WHERE quantidade > 1;

                            """
                        cursor.executescript(comando_DML_Update)
                        
                        conexao.commit()
                        # conexao.close()

                        print("Alterado Dados")

                        desejaInserirDeletar = True    

                    
                    elif insereDeleta == 4:
                        desejaInserirDeletar = False


                    else:
                        print(f"O numero {insereDeleta} que você digitou não faz parte das opções fornecidas")
                        desejaInserirDeletar = True

                                  
                else:
                    print(f"O numero {novosDados} que você digitou não faz parte das opções fornecidas")
                    desejaDeletar = True
            
            repeticao = True


#            numeroTabelas = numeroTabelas + 1


    elif criarTabela == 2:
        print("Ok, não será criado novas tabelas!")
    
    else:
        print("Não foi informado uma opção valida!")


    #Deletando tabelas
    deletarTabela = int(input(f"Deseja deletar uma tabela?\nDigite 1 para Sim e 2 para Não: "))

    if deletarTabela == 1:
        comando_DDL = """
                DROP TABLE IF EXISTS pedidos;
                DROP TABLE IF EXISTS produtos;
                DROP TABLE IF EXISTS categorias;
                DROP TABLE IF EXISTS fornecedor;
                DROP TABLE IF EXISTS clientes;
                """

        cursor.executescript(comando_DDL)
        conexao.commit()


        print("TABELAS DELETADAS!")

    
    elif deletarTabela == 2:
        print("Ok, não será deletado nenhuma tabela!")
    
    else:
        print("Não foi informado uma opção valida!")


    loop = True



