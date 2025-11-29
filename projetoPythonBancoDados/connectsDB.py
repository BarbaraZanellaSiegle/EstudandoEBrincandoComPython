import sqlite3

conexao = sqlite3.connect('VamosBricar.sqlite')
cursor = conexao.cursor()

conexao.commit()
conexao.close()
    
