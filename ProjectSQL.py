import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='jogos',
    user='root',
    password='mysql123')

if conexao.is_connected():
    print("Conectado!")
    cursor = conexao.cursor()

# cursor.execute('SELECT * FROM info')
# r = cursor.fetchall()
# for x in r:
#     print(x)

# cursor.execute('SELECT * FROM info')
# r = cursor.fetchone()
# print(r)

# sql = "INSERT INTO info (id, nome_jogos, genero, data_lancamento, console, unidadesvendidasEmMilhoes) VALUES ('11','Teste','Aventura','2020-10-03','PC','5')"
# cursor.execute(sql)
# conexao.commit()
# print(cursor.rowcount, 'Linha inserida.')

# sql = "DELETE FROM info WHERE nome_jogos = 'TESTE' "
# cursor.execute(sql)
# conexao.commit()
# print(cursor.rowcount, 'Linha deletada.')

conexao.close()
cursor.close()
