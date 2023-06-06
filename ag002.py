from Banco import Banco


host = '127.0.0.1'
user = 'root'
password = 'root'

db = Banco(host, user, password)

db.criarBanco()
